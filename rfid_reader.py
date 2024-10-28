import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
from repositories.RFIds import RFIdsRepository
from os import system
from utils.isAboveTenPercent import isAboveTenPercent

DEC_ID = 291543776768
INC_ID = 1032739306

idStorage = RFIdsRepository()
rfidReader = SimpleMFRC522()

count = 0

try:

    maxValue = int(input('Qual o total de pessoas permitidas? '))

    while(True):
        
        system("clear")
        print(f'Contador: {count}')
        
        tag, text = rfidReader.read()
        sleep(1)

        if(INC_ID == tag and isAboveTenPercent(count + 1, maxValue)):
            count += 1
        elif(tag != INC_ID and count != 0):
            count -= 1
        
except:
    print("DEU RUIM")
finally:
    print(idStorage.getAll())
    GPIO.cleanup()
