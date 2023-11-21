from time import sleep
import json
from datetime import date

with open('settings.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

URL_ACESS = data['url']
SCHEDULES = data['horarios']
PATH_PHOTOS = data['caminho_fotos']
FOLDER = data['pasta']
DATE = data['data']
POSITION = [(140,657),(297,668),(427,658),(566,671),(707,667),(841,673),(985,661)]
DAY = date.today().weekday()
TIMES = data['vezes']
LICENSE = 'KSK@KLA@#$!Q@#$AKDUJ'
MESSAGES = data['mensagens']