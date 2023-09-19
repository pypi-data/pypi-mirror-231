# coding: utf-8
u"""Кнопка "Запросить СНИЛС" для встраивания в формы."""
from __future__ import absolute_import
from types import NoneType
import json
import os

from django.template import Context
from django.template import Template

from edupfr._m3_imports import BaseExtField
from edupfr._m3_imports import ControllerCache
from edupfr._m3_imports import ExtButton
from .actions import SnilsRequestPack


class SnilsRequestButton(ExtButton):

    u"""Кнопка "Запросить СНИЛС".

    При необходимости использования данной кнопки должен быть зарегистрирован
    в системе actions.SnilsRequestPack.
    """

    def __init__(self, snils_field, last_name_field, first_name_field,
                 patronymic_field, date_of_birth_field, gender_field=None,
                 gender_choices=None, dul_number_field=None,
                 dul_date_field=None, *args, **kwargs):
        u"""Конструктор класса.

        :param snils_field: поле для ввода СНИЛС
        :param last_name_field: поле для ввода фамилии
        :param first_name_field: поле для ввода имени
        :param patronymic_field: поле для ввода отчества
        :param date_of_birth_field: поле для ввода даты рождения
        :param gender_field: поле для выбора пола
        :param gender_choices: словарь с соответствиями значений поля для ввода
            пола параметрами веб-сервиса, например
            {
                DelegateTypeEnumerate.FATHER: GENDER_MALE,
                DelegateTypeEnumerate.MATHER: GENDER_FEMALE,
                DelegateTypeEnumerate.LEX: None,
            }
        :param dul_number_field: поле для ввода номера документа,
            удостоверяющего личность
        :param dul_date_field: поле для ввода даты выдачи документа,
            удостоверяющего личность
        :param kwargs: остальные параметры для кнопки

        :type snils_field: subclass of BaseExtField
        :type last_name_field: subclass of BaseExtField
        :type first_name_field: subclass of BaseExtField
        :type patronymic_field: subclass of BaseExtField
        :type date_of_birth_field: subclass of BaseExtField
        :type gender_field: subclass of BaseExtField
        :type gender_choices: dict
        :type dul_number_field: subclass of BaseExtField
        :type dul_date_field: subclass of BaseExtField
        """
        # контроль типов данных аргументов
        assert isinstance(snils_field, BaseExtField), \
            type(snils_field)
        assert isinstance(last_name_field, BaseExtField), \
            type(last_name_field)
        assert isinstance(first_name_field, BaseExtField), \
            type(first_name_field)
        assert isinstance(patronymic_field, BaseExtField), \
            type(patronymic_field)
        assert isinstance(gender_field, (BaseExtField, NoneType)), \
            type(gender_field)
        assert gender_field is not None and \
            isinstance(gender_choices, (dict, NoneType)), \
            type(gender_choices)
        assert isinstance(dul_number_field, (BaseExtField, NoneType)), \
            type(dul_number_field)
        assert isinstance(dul_date_field, (BaseExtField, NoneType)), \
            type(dul_date_field)
        # если указано поле для выбора пола, то должен быть указан и словарь
        # с соответствиями
        assert not gender_field or gender_field and gender_choices
        # если указываются поля для ввода данных документа, то они должны быть
        # указаны все, либо ни одного
        assert dul_number_field is not None and dul_date_field is not None

        super(SnilsRequestButton, self).__init__(*args, **kwargs)

        self.snils_field = snils_field
        self.last_name_field = last_name_field
        self.first_name_field = first_name_field
        self.patronymic_field = patronymic_field
        self.date_of_birth_field = date_of_birth_field
        self.gender_field = gender_field
        self.gender_choices = gender_choices
        if gender_choices:
            self.gender_choices_json = json.dumps(gender_choices)
        else:
            self.gender_choices_json = None
        self.dul_number_field = dul_number_field
        self.dul_date_field = dul_date_field

        pack = ControllerCache.find_pack(SnilsRequestPack)
        action = pack.snils_request_action
        self.snils_request_action_url = action.get_absolute_url()

        self.handler = self._render_handler()

        if not self.text:
            self.text = u'Запросить СНИЛС'

    def _render_handler(self):
        self.pre_render_globals()

        template_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'snils-request-button.js')
        )

        with open(template_path, 'r') as template_file:
            template = Template(template_file.read())

        js = template.render(Context(dict(component=self)))

        return js
