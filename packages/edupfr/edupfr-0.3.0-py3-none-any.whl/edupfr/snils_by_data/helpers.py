# coding: utf-8
u"""Вспомогательные средства для работы с веб-сервисом PFRFsnilsbydata."""
from __future__ import absolute_import
import six
from collections import defaultdict
from datetime import date
from datetime import datetime
from traceback import format_exc
from six.moves.urllib.error import URLError
import os

from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone as tz
from spyne_smev.client import Client
from suds import WebFault
import suds.xsd.doctor
import suds.xsd.sxbasic

from . import InitializationError
from . import _log_request, _suds_plugins
from . import settings

# Пол
GENDER_MALE = u'M'  # мужской
GENDER_FEMALE = u'F'  # женский

# Результаты выполнения запроса к веб-сервису
RC_FOUND = 0  # СНИЛС найден
RC_NOT_FOUND = 1  # СНИЛС не найден
RC_MULTIPLE_FOUND = 2  # найдено несколько СНИЛС
RC_ERROR = 3  # ошибка во время выполнения запроса к веб-сервису

# Результаты обработки записей модели при загрузке в нее СНИЛС
LOAD_RC_UPDATED = 0  # СНИЛС найден и сохранен в записи
LOAD_RC_NO_DATA = 1  # Запись не содержит обязательных для запроса данных
LOAD_RC_NOT_FOUND = 2  # СНИЛС не найден

# коды возврата веб-сервиса
WSRC_SNILS_NOT_FOUND = 'SKMV-SNILS-0003'


def _get_wsdl_url():
    if not settings.WSDL_URL:
        raise InitializationError('WSDL URL required')

    return settings.WSDL_URL


def _get_private_key_path():
    if not settings.SMEV_PRIVATE_KEY_FILE_PATH:
        return None

    if not os.path.exists(settings.SMEV_PRIVATE_KEY_FILE_PATH):
        raise ImproperlyConfigured(
            'SMEV private key file (%s) not found' %
            settings.SMEV_PRIVATE_KEY_FILE_PATH
        )

    return settings.SMEV_PRIVATE_KEY_FILE_PATH


def _get_certificate_path():
    if not settings.SMEV_CERTIFICATE_FILE_PATH:
        return None

    if not os.path.exists(settings.SMEV_CERTIFICATE_FILE_PATH):
        raise ImproperlyConfigured(
            'SMEV certificate file (%s) not found' %
            settings.SMEV_CERTIFICATE_FILE_PATH
        )

    return settings.SMEV_CERTIFICATE_FILE_PATH


def _get_client():
    u"""Возвращает клиента веб-сервиса.

    URL описания веб-сервиса берется из конфигурации системы, параметр
        [webservice.pfr.snils_by_data]
        WSDL_URL = ...

    Пути к файлам с закрытым ключом и сертификатом также берутся из
    конфигурации.

    Клиент создается с плагином журналирования запросов и ответов, данные
    будут сохраняться в модель
    kinder.webservice.smev.decl_status_sync.models.SmevLogs

    :rtype: spyne_smev.client.Client
    """
    wsdl_url = _get_wsdl_url()

    # т.к. suds некорректно обрабатывает импорт внешней XML-схемы, приходится
    # делать это вручную
    pfr_namespace_uri = 'http://pfr.skmv.rstyle.com'
    doctor = None
    proxy_params = {}
    if settings.PROXY_PARAMS:
        proxy_params.update({'proxy': dict(http=settings.PROXY_PARAMS,
                                           https=settings.PROXY_PARAMS)})

    client = Client(wsdl_url, **proxy_params)
    for import_node in client.wsdl.schema.imports:
        if isinstance(import_node, suds.xsd.sxbasic.Import):
            _, namespace_uri = import_node.ns
            if namespace_uri == pfr_namespace_uri:
                doctor = suds.xsd.doctor.ImportDoctor(
                    suds.xsd.doctor.Import(
                        pfr_namespace_uri, import_node.location
                    )
                )
                break

    client = Client(
        url=wsdl_url,
        location=settings.LOCATION,
        private_key_path=_get_private_key_path(),
        private_key_pass=settings.SMEV_PRIVATE_KEY_PASSWORD,
        certificate_path=_get_certificate_path(),
        doctor=doctor,
        plugins=_suds_plugins,
        **proxy_params
    )

    return client


def _build_request_params(client, last_name, first_name, patronymic, gender,
                          date_of_birth):
    u"""Заполняет Message и MessageData параметрами."""
    message = client.factory.create('SnilsByDataRequest.Message')
    message.Sender.Code = settings.SMEV_CLIENT_ID
    message.Sender.Name = u'БАРС Электронный детский сад'
    message.Recipient.Code = u'PFRF01001'
    message.Recipient.Name = u'Пенсионный фонд РФ'

    message.Service = (
        client.factory.create('{http://smev.gosuslugi.ru/rev120315}Service')
    )
    message.Service.Mnemonic = u'SNILS_BY_DATA'
    message.Service.Version = u'1.00'
    # Тип сообщения (Взаимодействие в рамках оказания государственных услуг)
    message.TypeCode = u'GSRV'
    # код 2 (Межведомственное взаимодействие)
    message.ExchangeType = u'2'
    # Дата и время формирования запроса
    message.Date = datetime.now(tz.get_current_timezone()).isoformat()
    message.Status = u'REQUEST'

    data = client.factory.create('SnilsByDataIn')
    data.fio.FirstName = first_name
    data.fio.LastName = last_name
    data.fio.Patronymic = patronymic or None
    data.gender = gender
    data.birthDate = date_of_birth.strftime('%d-%m-%Y')

    message_data = client.factory.create('SnilsByDataRequest.MessageData')
    message_data.AppData.request = [data]

    return message, message_data


class _SendRequestError(Exception):
    pass


def _send_request(client, message, message_data):
    u"""Отправка запроса к веб-сервису ПФР и возвращает результат.

    :raises _SendRequestError: если возникла ошибка при отправке запроса, либо
        во время его выполнения
    """
    try:
        response = client.service.SnilsByDataRequest(message, message_data)
    except WebFault as error:
        _log_request(client,
                     u'\n'.join((error.fault.faultstring,
                                 six.text_type(format_exc(), errors='replace'))))
        raise _SendRequestError(error.fault.faultstring)
    except URLError as error:
        raise _SendRequestError(
            u'Нет доступа к веб-сервису ПФР (%s)' % six.text_type(error)
        )
    except Exception as error:
        _log_request(client, error.message)
        raise _SendRequestError(error.message)
    else:
        _log_request(client)

    if hasattr(response.MessageData.AppData, 'fault'):
        # В связи с особенностями описания xml-схемы suds все данные из ответа
        # размещает в одноэлементных списках, поэтому приходится обращаться
        # к данным через нулевой элемент списка.
        error_code = response.MessageData.AppData.fault[0].code[0]
        if error_code != WSRC_SNILS_NOT_FOUND:
            error_message = response.MessageData.AppData.fault[0].message[0]
            raise _SendRequestError(error_message)

    return response


def _extract_data_from_response(response):
    u"""Извлекает данные из результата выполнения запроса.

    :return:
        - None, если СНИЛС не найден,
        - строку, содержащую СНИЛС, если СНИЛС был найден,
        - словарь, если найдено несколько СНИЛС (ключ - СНИЛС, значение
          ключа - список из кортежей (номер документа, дата выдачи))
    :rtype: unicode or dict
    """
    app_data = response.MessageData.AppData

    if hasattr(app_data, 'fault'):
        # Сервис вернул сообщение об ошибке, но до этого места доходит только
        # сообщение о том, что "СНИЛС не найден".
        return None

    # В связи с особенностями описания xml-схемы suds все данные из ответа
    # размещает в одноэлементных списках, поэтому приходится обращаться
    # к данным через нулевой элемент списка.
    response_result = app_data.result[0]

    if hasattr(response_result, 'twinData'):
        # найдены несколько СНИЛСов
        result = defaultdict(list)
        for data in response_result.twinData:
            snils = data.twinSnils[0]
            for doc in data.twinDocument[0].document:
                doc_number = doc.number[0]
                doc_date = datetime.strptime(doc.issueDate[0],
                                             '%Y-%m-%d').date()
                result[snils].append((doc_number, doc_date))
    else:
        # найден единственный СНИЛС
        snils = response.MessageData.AppData.result[0].snils[0]
        result = snils

    return result


def get_snils(last_name, first_name, patronymic, gender, date_of_birth,
              dul_number=None, dul_date=None):
    u"""Возвращает СНИЛС по данным физ. лица.

    СНИЛС запрашивается у веб-сервиса ПФР.

    :param unicode last_name: Фамилия
    :param unicode first_name: Имя
    :param patronymic: Отчество
    :param gender: Пол (GENDER_MALE или GENDER_FEMALE). Если None, то
        будет выполнено два запроса для мужского и женского пола.
    :param date_of_birth: Дата рождения
    :param dul_number: Номер документа, удостоверяющего личность
    :param dul_date: Дата выдачи документа, удостоверяющего личность

    :type patronymic: unicode or None
    :type gender: unicode or None
    :type date_of_birth: datetime.date
    :type dul_number: unicode or None
    :type dul_date: unicode or None

    :return: Кортеж из двух элементов: 1-й элемент - СНИЛС или сообщение об
        ошибке, 2-й элемент - код возврата.

        Если найден СНИЛС, то его значение будет в первом элементе, а код
        возврата - RC_FOUND.

        Если же СНИЛС не найден, то первый элемент кортежа будет None, а
        второй - RC_NOT_FOUND или RC_MULTIPLE_FOUND.

        Если во время выполнения запроса к веб-сервису возникла ошибка, первым
        элементом кортежа будет сообщение об ошибке, а вторым - RC_ERROR.
    :rtype: tuple(unicode or None, unicode or None)
    """
    assert isinstance(last_name, six.text_type) and last_name, repr(last_name)
    assert isinstance(first_name, six.text_type) and first_name, repr(first_name)
    assert (patronymic is None or
            isinstance(patronymic, six.text_type) and patronymic), repr(patronymic)
    assert (gender is None or
            gender in (GENDER_MALE, GENDER_FEMALE)), repr(gender)
    assert isinstance(date_of_birth, date), repr(date_of_birth)
    assert (dul_number is None or
            isinstance(dul_number, six.text_type) and dul_number), repr(dul_number)
    assert dul_date is None or isinstance(dul_date, date), repr(dul_date)
    # если указана дата выдачи документа, то номер документа тоже должен быть
    assert dul_date is None or dul_number is not None

    if not settings._initialized:
        raise ImproperlyConfigured('Package edupfr.snils_by_data not '
                                   'initialized.')

    client = _get_client()
    gender_list = (gender,) if gender is not None else (GENDER_MALE,
                                                        GENDER_FEMALE)
    data = defaultdict(list)
    for _gender in gender_list:
        message, message_data = _build_request_params(
            client, last_name, first_name, patronymic, _gender, date_of_birth
        )

        try:
            response = _send_request(client, message, message_data)
        except _SendRequestError as error:
            return six.text_type(error), RC_ERROR

        response_data = _extract_data_from_response(response)
        if response_data is None:
            if gender is not None:
                return None, RC_NOT_FOUND
            else:
                continue
        elif isinstance(response_data, six.string_types):
            return response_data, RC_FOUND
        else:
            for snils, documents in six.iteritems(response_data):
                data[snils].extend(documents)

    if not data:
        return None, RC_NOT_FOUND
    elif dul_number is None:
        return None, RC_MULTIPLE_FOUND

    for snils, documents in six.iteritems(data):
        for doc_number, doc_date in documents:
            if (dul_number == doc_number and
                    (dul_date is None or dul_date == doc_date)):
                return snils, RC_FOUND

    return None, RC_NOT_FOUND


def load_snils_for_objects(objects, field_names, gender_lookup=None,
                           handler=None):
    u"""Запрашивает СНИЛС для нескольких объектов.

    Для каждого объекта из *objects* запрашивает через веб-сервис ПФР СНИЛС
    застрахованного лица, данные которого содержатся в объекте. Соответствие
    параметров запроса и полей объекта указывается в *field_names*.

    Т.к. обязательными параметрами запроса к веб-сервису ПФР являются фамилия,
    имя и дата рождения застрахованного, записи с пустыми значениями этих полей
    будут пропущены при обработке.

    Если не указывается поле, содержащее пол застрахованного, то на каждую
    запись будет отправляться до двух запросов по одному на каждый пол. Если в
    первом запросе СНИЛС будет найден, второй запрос выполняться не будет.

    Обработка результатов запроса должна осуществляться в callable-объекте
    *handler*, который вызывается после выполнения запроса для каждого объекта
    из *objects*.

    :param iterable objects: Экземпляры модели Django, для которых нужно
        запросить СНИЛС.
    :param dict field_names: Словарь с именами полей модели. Должен иметь
        следующий вид:
            {
                'last_name_field': 'имя поля Фамилия',
                'first_name_field': 'имя поля Имя',
                'middle_name_field': 'имя поля Отчество',
                'date_of_birth_field': 'имя поля Дата рождения',
                'gender_field': 'имя поля Пол',
                'dul_number_field': 'имя поля Номер документа',
                'dul_date_field': 'имя поля Дата выдачи документа',
            }
        Поля СНИЛС, фамилия, имя и дата рождения обязательные.
    :param dict gender_lookup: Словарь соответствия значений поля Пол значениям
        аргумента *gender* функции *get_snils()*.
    :param callable handler: Функция для обработки результатов каждого запроса
        к веб-сервису. В качестве аргументов функция должна принимать экземпляр
        модели, результат его обработки и СНИЛС, если найден. В эту функцию
        могут быть переданы следующие значения результата обработки:
            LOAD_RC_UPDATED - в объекте модели сохранен СНИЛС;
            LOAD_RC_NO_DATA - в объекте модели не хватает данных для запроса;
            LOAD_RC_NOT_FOUND - СНИЛС не найден.

    Пример использования:

        class Student(Model):
            last_name = models.CharField(...)
            first_name = models.CharField(...)
            patronymic = models.CharField(...)
            gender = models.BooleanField(...)
            date_of_birth = models.DateField(...)
            snils = models.CharField(...)

        def handler(obj, result_code, snils):
            if snils is not None:
                # сохранение результата выполнения запроса к веб-сервису
                obj.snils = snils
                obj.save()
                print snils

        objects = Student.objects.all().iterator()
        field_names = dict(
            snils_field='snils',
            last_name_field='last_name',
            first_name_field='first_name',
            middle_name_field='patronymic',
            date_of_birth_field='date_of_birth',
            gender_field='gender',
        )
        gender_lookup={
            True: GENDER_MALE,
            False: GENDER_FEMALE,
            None: None
        }
        load_snils_for_model(objects, field_names, gender_lookup, handler)
    """
    for obj in objects:
        last_name = getattr(obj, field_names['last_name_field'])
        first_name = getattr(obj, field_names['first_name_field'])
        date_of_birth = getattr(obj, field_names['date_of_birth_field'])

        if not all((last_name, first_name, date_of_birth)):
            handler(obj, LOAD_RC_NO_DATA, None)
            continue

        patronymic = None
        if 'middle_name_field' in field_names:
            patronymic = getattr(obj, field_names['middle_name_field'])

        gender = None
        if 'gender_field' in field_names:
            gender = getattr(obj, field_names['gender_field'])
            if gender_lookup is not None:
                gender = gender_lookup[gender]

        dul_number = None
        if 'dul_number_field' in field_names:
            dul_number = getattr(obj, field_names['dul_number_field'])

        dul_date = None
        if 'dul_date_field' in field_names:
            dul_date = getattr(obj, field_names['dul_date_field'])

        snils, result_code = get_snils(last_name, first_name, patronymic,
                                       gender, date_of_birth, dul_number,
                                       dul_date)
        if result_code == RC_FOUND:
            handler(obj, LOAD_RC_UPDATED, snils)
        else:
            handler(obj, LOAD_RC_NOT_FOUND, None)
