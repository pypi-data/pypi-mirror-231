# coding: utf-8
u"""Импорты объектов m3."""
from __future__ import absolute_import
import m3


if hasattr(m3, 'VERSION') and m3.VERSION[0] == 0:
    # это ЭДС, ветка dou_tatar, версия m3<1.0.0
    from m3.ui.actions.context import ActionContextDeclaration as ACD
    from m3.ui.actions.results import OperationResult
    from m3.ui.actions import ControllerCache
    from m3.ui.ext.controls.buttons import ExtButton
    from m3.ui.ext.fields.base import BaseExtField
else:
    from m3.actions.context import ActionContextDeclaration as ACD
    from m3.actions.results import OperationResult
    from m3.actions import ControllerCache
    from m3_ext.ui.controls.buttons import ExtButton
    from m3_ext.ui.fields.base import BaseExtField
