import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
from repositories.RFIds import RFIdsRepository
from os import system
import serial

DEC_ID = 291543776768
INC_ID = 1032739306

idStorage = RFIdsRepository()
rfidReader = SimpleMFRC522()
serial = serial.Serial('/dev/ttyACM0', 9600)

count = 0

try:

    maxValue = int(input('Qual o total de pessoas permitidas? '))
    maxValueMoreTenPercent = int(maxValue + (maxValue * 0.1))

    while(True):
        
        system("clear")
        print(f'Contador: {count}')

        if serial.in_waiting > 0:
            print(serial.readline())
        
        tag, text = rfidReader.read()
        sleep(1)

        if(INC_ID == tag):
            count += 1
        elif(tag != INC_ID and count != 0):
            count -= 1
            
        serial.write(f'{count} {maxValueMoreTenPercent}'.encode('utf-8'))
        serial.reset_input_buffer()

        if(count > maxValueMoreTenPercent):
            count = maxValueMoreTenPercent

except:
    print("Parando operações...")
finally:
    serial.close()
    GPIO.cleanup()
