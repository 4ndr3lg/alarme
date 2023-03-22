import datetime #Biblioteca padrão pra obter a hora do sistema
import time #biblioteca padrão para agendar o alarme
import pyautogui
from playsound import playsound #biblioteca playsound tem que ser instalada manualmente e é a responsavel por tocar o som do alarme

hora_do_despertar = input("Digite a hora de despertar no formato HH:MM: ")

try:
    hora, minuto = hora_do_despertar.split(":")
    hora = int(hora)
    minuto = int(minuto)
    assert 0 <= hora < 24
    assert 0 <= minuto < 60
except:
    print("Entrada invalida. Use o formato HH:MM")
    exit()

while True:
    agora = datetime.datetime.now()
    if agora.hour == hora and agora.minute == minuto:
        print("VAMOOOO ACORDAAAAAAA!!!")
        pyautogui.PAUSE = 3.0
        pyautogui.press('win')
        pyautogui.write('spotify')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.moveTo(300, 217)
        time.sleep(3)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1219, 171)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('Alarme')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.moveTo(672, 360)
        pyautogui.click()
        break
    time.sleep(60)