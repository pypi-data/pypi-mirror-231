# coding: utf-8
u"""Паки и экшены для кнопки "Запросить СНИЛС"."""
from __future__ import absolute_import
import six
from datetime import date

from objectpack.actions import BaseAction
from objectpack.actions import BasePack

from edupfr._m3_imports import ACD
from edupfr._m3_imports import OperationResult
from edupfr.snils_by_data.helpers import GENDER_FEMALE
from edupfr.snils_by_data.helpers import GENDER_MALE
from edupfr.snils_by_data.helpers import RC_ERROR
from edupfr.snils_by_data.helpers import RC_FOUND
from edupfr.snils_by_data.helpers import RC_MULTIPLE_FOUND
from edupfr.snils_by_data.helpers import RC_NOT_FOUND
from edupfr.snils_by_data.helpers import get_snils


class SnilsRequestAction(BaseAction):

    u"""Action для отправки запроса в ПФР и возврата результата в UI."""

    def context_declaration(self):
        return [
            ACD(name='last_name', type=six.text_type, required=True,
                verbose_name=u'Фамилия'),
            ACD(name='first_name', type=six.text_type, required=True,
                verbose_name=u'Имя'),
            ACD(name='patronymic', type=six.text_type, required=False,
                verbose_name=u'Отчество'),
            ACD(name='gender', type=six.text_type, required=False,
                verbose_name=u'Пол'),
            ACD(name='date_of_birth', type=date, required=True,
                verbose_name=u'Дата рождения'),
            ACD(name='dul_number', type=six.text_type, required=False,
                verbose_name=u'Номер документа'),
            ACD(name='dul_date', type=date, required=False,
                verbose_name=u'Дата выдачи документа'),
            ACD(name='has_dul_fields', type=bool, required=True,
                default=False),
        ]

    def run(self, request, context):
        # обработка входных параметров
        last_name = context.last_name
        first_name = context.first_name
        date_of_birth = context.date_of_birth
        patronymic = getattr(context, 'patronymic', None) or None
        gender = getattr(context, 'gender', None) or None
        dul_number = getattr(context, 'dul_number', None) or None
        dul_date = getattr(context, 'dul_date', None) or None

        # проверка корректности входных параметров
        error_message = None

        if not last_name:
            error_message = u'Не указана фамилия'
        elif not first_name:
            error_message = u'Не указано имя'
        elif not date_of_birth:
            error_message = u'Не указана дата рождения'
        elif gender and gender not in (GENDER_MALE, GENDER_FEMALE):
            error_message = u'Некорректно указан пол (%s)' % gender
        elif dul_date is not None and dul_number is None:
            error_message = u'Не указан номер документа'

        if error_message is not None:
            return OperationResult(success=False, message=error_message)

        # отправка запроса в ПФР
        data, result_code = get_snils(
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
            gender=gender,
            date_of_birth=date_of_birth,
            dul_number=dul_number,
            dul_date=dul_date
        )

        if result_code == RC_FOUND:
            return OperationResult(code='"%s"' % data)
        elif result_code == RC_NOT_FOUND:
            error_message = u'СНИЛС не найден.'
        elif result_code == RC_MULTIPLE_FOUND:
            if context.has_dul_fields:
                error_message = (
                    u'Найдено несколько застрахованных лиц, для уточнения '
                    u'запроса попробуйте указать номер и дату выдачи '
                    u'документа, удостоверяющего личность.'
                )
            else:
                error_message = (
                    u'Не удалось определить СНИЛС, т.к. найдено несколько '
                    u'застрахованных лиц.'
                )
        elif result_code == RC_ERROR:
            error_message = data
        else:
            raise ValueError('Unsupported result code: %r' % result_code)

        return OperationResult(success=False, message=error_message)


class SnilsRequestPack(BasePack):

    u"""Пак для кнопки "Запросить СНИЛС"."""

    def __init__(self):
        u"""Конструктор пака.

        Создает Action для отправки запроса в ПФР и возврата результата в UI.
        """
        super(SnilsRequestPack, self).__init__()

        self.snils_request_action = SnilsRequestAction()
        self.actions.append(self.snils_request_action)
