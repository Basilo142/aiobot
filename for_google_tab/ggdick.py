# Подключаем библиотеки
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'my-python-bot-328407-69e1fddb1efa.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [
    'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'
])

httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API

# spreadsheet = service.spreadsheets().create(body={
#     'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
#     'sheets': [{'properties': {'sheetType': 'GRID',
#                                'sheetId': 0,
#                                'title': 'Лист номер один',
#                                'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
# }).execute()
# spreadsheetId = spreadsheet['spreadsheetId']  # сохраняем идентификатор файла
# print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)

# driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
# access = driveService.permissions().create(
#     fileId = spreadsheetId,
#     body = {'type': 'user', 'role': 'writer', 'emailAddress': 'basilomail@gmail.com'},  # Открываем доступ на редактирование
#     fields = 'id'
# ).execute()
spreadsheetId = '1XeKFTCe7ZieVJ40h-jr6kGz8dH1K2IVoLJMAegXb0-8'
sp2 = '1T0I1AWS17rVRiA9L9v5ckFFR2obKQFmGERjy91eo6YQ'
results = service.spreadsheets().values().batchUpdate(spreadsheetId=sp2, body={
    "valueInputOption": "USER_ENTERED",  # Данные воспринимаются, как вводимые пользователем (считается значение формул)
    "data": [
        {"range": "Март!B2:D5",
         "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
         "values": [
                    ["Ячейка B2"]  # Заполняем вторую строку
                   ]}
    ]
}).execute()

# ranges = ['Ноябрь 2021!B1:B1']
# result = service.spreadsheets().values().batchGet(spreadsheetId=sp2, ranges=ranges,
#                                                   valueRenderOption='FORMATTED_VALUE',
#                                                   dateTimeRenderOption='FORMATTED_STRING').execute()
# print('result=', result)
# sheet_values = int(result['valueRanges'][0]['values'][0][0])
#
# print('sheet_values', sheet_values)
# s = sheet_values+0
# print(s)

