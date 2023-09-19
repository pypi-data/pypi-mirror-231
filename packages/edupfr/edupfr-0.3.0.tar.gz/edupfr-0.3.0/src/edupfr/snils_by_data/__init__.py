# coding: utf-8
u"""Функионал для работы с веб-сервисом ПФ РФ для запроса СНИЛС по ФИО и ДР.

Мнемоника сервиса:
    PFRFsnilsbydata.
Наименование:
    Сервис предоставления СНИЛС по данным лицевого счета.
Основное назначение:
    Электронный сервис предназначен для обеспечения возможности получения
    страхового номера индивидуального лицевого счета (СНИЛС), соответствующего
    представленным данным лицевого счета застрахованного лица.
Описание функционала:
    https://conf.bars-open.ru/pages/viewpage.action?pageId=1246641

Пакет содержит:
    1. Функцию helpers.get_snils() для отправки запроса к веб-сервису и
       получения результата.
    2. Кнопку "Запросить СНИЛС" для встраивания в формы (для использования
       необходима регистрация в системе пака actions.SnilsRequestPack).

Перед использованием пакет необходимо проинициализировать. Для этого следует
использовать функцию edupfr.snils_by_data.initialize().
"""
from __future__ import absolute_import
from edupfr.snils_by_data import settings


class InitializationError(Exception):
    u"""Ошибка инициализации пакета."""


def initialize(config, log_func=None, controller=None):
    u"""Инициализация пакета.

    :param dict config: Словарь, содержащий следующие параметры конфигурации
        пакета:
            - WSDL_URL (адрес описания веб-сервиса),
            - SMEV_PRIVATE_KEY_FILE_PATH (путь к файлу с закрытым ключом),
            - SMEV_PRIVATE_KEY_PASSWORD (пароль к закрытому ключу),
            - SMEV_CERTIFICATE_FILE_PATH (путь к файлу с сертификатом),
            - SMEV_CLIENT_ID (мнемоника системы -клиента в СМЭВ, идентификатор
              системы в СМЭВ),
            - PROXY_PARAMS (параметры прокси-сервера, необязательный).
            - LOCATION параметр location в suds.client - адрес куда будет отправлен запрос,
            необязательный параметр, по умолчанию запрос уйдет на адрес указанный в WSDL_URL
            - SUDS_PLUGINS Список плагинов, наследников suds.plugin.MessagePlugin, необязательный параметр
    :param log_func:
        callable-объект, принимающий два параметра:
            - client - экземпляр spyne_smev.client.Client, используемый для
                выполнения запроса к веб-сервису
            - error=None - сообщение об ошибке
    :param controller: контроллер M3, в котором будет регистрироваться
        SnilsRequestPack. Нужно для работы кнопки "Запросить СНИЛС".

    Пример использования:

        from edupfr.snils_by_data import initialize
        from edupfr.snils_by_data.helpers import METHOD_NAME
        from kinder.settings import conf
        from kinder.controllers import dict_kontroller

        def log_request(client, error=None):
            SmevLogs.objects.create(
                smev_method=METHOD_NAME,
                direction=SmevMethods.OUTGOING,
                request=client.last_sent(),
                response=client.last_received(),
                error=error,
            )

        config = dict(
            WSDL_URL=conf.get('pfr.snils_by_data', 'WSDL_URL'),
            SMEV_PRIVATE_KEY_FILE_PATH=conf.get('kinder', 'SMEV_PRIVATE_KEY'),
            SMEV_PRIVATE_KEY_PASSWORD=conf.get('kinder',
                                               'SMEV_PRIVATE_KEY_PASSWORD'),
            SMEV_CERTIFICATE_FILE_PATH=conf.get('kinder', 'SMEV_CERTIFICATE'),
            SMEV_CLIENT_ID=conf.get('kinder', 'SMEV_SYS_MNEMONICS'),
        )

        initialize(config, log_request, dict_controller)

    ВНИМАНИЕ! При использовании асинхронных заданий Celery одним из мест, где
    можно инициализировать пакет, является обработчик сигнала
    celery.signals.worker_init.
    """
    global _suds_plugins
    assert log_func is None or callable(log_func), repr(log_func)

    required_params = ('WSDL_URL', 'SMEV_CLIENT_ID')
    optional_params = ('PROXY_PARAMS', 'SMEV_PRIVATE_KEY_FILE_PATH', 'SMEV_PRIVATE_KEY_PASSWORD',
                       'SMEV_CERTIFICATE_FILE_PATH', 'METHOD_NAME', 'LOCATION', )

    for param in required_params:
        if param not in config:
            return
        setattr(settings, param, config[param])
    for param in optional_params:
        if param in config:
            setattr(settings, param, config[param])

    if 'SUDS_PLUGINS' in config:
        _suds_plugins.extend(config['SUDS_PLUGINS'])

    if log_func is not None:
        global _log_function
        _log_function = log_func

    if controller is not None:
        from .actions import SnilsRequestPack
        controller.packs.append(SnilsRequestPack())

    settings._initialized = True


# Функция для журналирования запросов к веб-серверу и ответов на эти запросы
_log_function = None
# Список плагинов для suds.Client
_suds_plugins = []


def _log_request(client, error=None):
    global _log_function
    if _log_function is not None:
        _log_function(client=client, error=error)
