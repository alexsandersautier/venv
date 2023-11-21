import webbrowser
import pyautogui as py
from time import sleep
import constant
from datetime import datetime, timedelta
import json
import pyperclip

i = int(constant.FOLDER)
day_publication = datetime.strptime(constant.DATE, '%d/%m/%Y').date()
hours = constant.SCHEDULES
SelectedDay = False
m = 1
for day in range(constant.TIMES):
    k = 0
    for hour in hours:
        if m > constant.MESSAGES[len(constant.MESSAGES)-1]:
            m = 1
        print(f'================Esta é a mensagem {m}=========')    
        with open(f'mensagem{m}.txt', encoding="utf8") as chat:
            chat_text = chat.read()
        print(chat_text)       

        k += 1
        m += 1