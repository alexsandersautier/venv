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
first = False
m = 0
try:
    for day in range(constant.TIMES):
        k = 0
        for hour in hours:
            if not first:
                webbrowser.open_new_tab(constant.URL_ACESS)
                first = True
            else:
                webbrowser.open(constant.URL_ACESS)
            sleep(10)  
            #click in select account
            py.hotkey('tab')
            py.hotkey('space')
            sleep(1)
            #unmade account facebook
            py.hotkey('space')
            #make account instagram
            py.hotkey('down')
            py.hotkey('space')
            py.hotkey('esc')
            #click add file
            py.hotkey('tab')
            py.hotkey('space')
            #load from pc
            py.hotkey('space')
            #write path
            sleep(1)
            caminho = constant.PATH_PHOTOS.replace('/','\\') + f'\\{str(i)}'
            sleep(2)
            i = i + 1
            print(i)
            pyperclip.copy(caminho)
            py.hotkey('ctrl','v')
            py.hotkey('enter')
            py.hotkey('tab')
            py.hotkey('t')
            py.hotkey('shift','tab')
            py.hotkey('shift','tab')
            py.hotkey('ctrl','a')
            py.hotkey('enter')
            sleep(7)
            #click message box
            py.hotkey('tab')
            #write message
            if m > constant.MESSAGES[len(constant.MESSAGES)-1]:
                m = 1
            with open(f'mensagem{constant.MESSAGES[m]}.txt', encoding="utf8") as chat:
                chat_text = chat.read()
            pyperclip.copy(chat_text)       
            py.hotkey('ctrl','v')        
            sleep(1)
            py.hotkey('esc')
            for w in range(3):
                py.hotkey('tab')
                sleep(1)
            #click define hour and date
            py.hotkey('space')
            sleep(1)
            py.hotkey('tab')
            py.hotkey('ctrl','a')
            py.write(day_publication.strftime('%d/%m/%Y'))
            #click hour
            py.hotkey('tab')
            sleep(1)
            if datetime.strptime(hours[k],'%H:%M').hour > 12:
                py.write(str(datetime.strptime(hours[k],'%H:%M').hour - 12))
            else:
                py.write(str(datetime.strptime(hours[k],'%H:%M').hour))
            sleep(1)
            #click minute
            py.hotkey('tab')
            sleep(1)
            py.write(str(datetime.strptime(hours[k],'%H:%M').minute))
            sleep(1)
            if datetime.strptime(hours[k],'%H:%M').hour > 12:
                py.hotkey('tab')
                sleep(1)
                py.write('PM')
            else:
                py.hotkey('tab')
                sleep(1)
                py.write('AM')
            k += 1
            m += 1
            #publication
            for x in range(5):
                py.hotkey('tab')
            py.hotkey('space')
            sleep(5)
            py.hotkey('ctrl','w')
            sleep(3)
            with open('settings.json', 'r', encoding='UTF-8') as file:
                data = json.load(file)   

            data['pasta'] = i

            with open('settings.json', 'w', encoding='UTF-8') as file:
                json.dump(data,file)  
        day_publication += timedelta(1)
except Exception as e:
    print(e)