import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
from repositories.RFIds import RFIdsRepository
from os import system
from utils.isAboveTenPercent import isAboveTenPercent
import serial

DEC_ID = 291543776768
INC_ID = 1032739306

idStorage = RFIdsRepository()
rfidReader = SimpleMFRC522()
serial = serial.Serial('/dev/ttyACM0', 9600)

count = 0

try:

    maxValue = int(input('Qual o total de pessoas permitidas? '))

    while(True):
        
        system("clear")
        print(f'Contador: {count}')

        if serial.in_waiting > 0:
            print(serial.readline())
        
        tag, text = rfidReader.read()
        sleep(1)

        if(INC_ID == tag and not isAboveTenPercent(count + 1, maxValue)):
            count += 1
        elif(tag != INC_ID and count != 0):
            count -= 1
            
        serial.write(f'{count}'.encode('utf-8'))
        serial.reset_input_buffer()

except:
    print("DEU RUIM")
finally:
    serial.close()
    GPIO.cleanup()
