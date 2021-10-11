import httplib2
import logging
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from data import config

CREDENTIALS_FILE = 'for_google_tab/my-python-bot-328407-69e1fddb1efa.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [
    'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'
])
httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
SERVICE = apiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API
SP_ID = config.SPREADSHEETID


def reading_data(ranges: list):  # ["Лист номер один!A2:F8"]
    result = SERVICE.spreadsheets().values().batchGet(spreadsheetId=SP_ID, ranges=ranges,
                                                      valueRenderOption='FORMATTED_VALUE',
                                                      dateTimeRenderOption='FORMATTED_STRING').execute()
    try:
        sheet_values = int(result['valueRanges'][0]['values'][0][0])
    except KeyError:
        sheet_values = 0
    return sheet_values


def adding_data(ranges: list, data: int):
    old_data = reading_data(ranges)
    new_data = old_data + data
    results = SERVICE.spreadsheets().values().batchUpdate(spreadsheetId=SP_ID, body={
        "valueInputOption": "USER_ENTERED",
        # Данные воспринимаются, как вводимые пользователем (считается значение формул)
        "data": [
            {"range": ranges[0],
             "majorDimension": "ROWS",  # Сначала заполнять строки, затем столбцы
             "values": [
                 [new_data]  # Заполняем строку (ячейку)
             ]}
        ]
    }).execute()
    return new_data
