# coding: utf-8
u"""Параметры пакета."""

_initialized = False

# Мнемоника сервиса
METHOD_NAME = 'SnilsByDataRequest'

# Адрес WSDL веб-сервиса.
WSDL_URL = None
# Адрес куда уходит запрос веб-сервиса
LOCATION = None
# Путь к файлу с закрытым ключом, используемым для подписывания запросов к
# СМЭВ.
SMEV_PRIVATE_KEY_FILE_PATH = None

# Пароль закрытого ключа.
SMEV_PRIVATE_KEY_PASSWORD = None

# Путь к файлу с сертификатом электронной подписи, используемым для проверки
# электронной подписи ответов на запрос к СМЭВ.
SMEV_CERTIFICATE_FILE_PATH = None

# Мнемоника (идентификатор) локальной системы в СМЭВ
SMEV_CLIENT_ID = None

# параметры прокси сервера
PROXY_PARAMS = None
