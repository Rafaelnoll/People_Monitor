// Programa: Display LCD 16x2 e módulo I2C
// Autor: Arduino e Cia

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Inicializa o display no endereço 0x27
LiquidCrystal_I2C lcd(0x27, 16, 2);

int ledPin = 8;
int buzzerPin = 7;

void setup() {
    Serial.begin(9600); 
    lcd.init();         
    lcd.backlight();    

    pinMode(ledPin, OUTPUT);
    pinMode(buzzerPin, OUTPUT);

    while (!Serial) {}; 
}

void loop() {
    if (Serial.available() > 0) { 
        String message = Serial.readString(); 

        int separatorIndex = message.indexOf(' ');
        String currentPeopleStr = message.substring(0, separatorIndex);
        String maxPeopleStr = message.substring(separatorIndex + 1);

        int currentPeople = 0;
        int maxPeople = 0;

        currentPeople = currentPeopleStr.toInt();
        maxPeople = maxPeopleStr.toInt();

        if (separatorIndex != -1) {

            currentPeople = message.substring(0, separatorIndex).toInt();
            maxPeople = message.substring(separatorIndex + 1).toInt();
        } else {
            return;
        }

        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Pessoas / Max");

        lcd.setCursor(0, 1);
        
        if(currentPeople <= maxPeople){
            lcd.print(String(currentPeople) + " / " + String(maxPeople));
        } else {
            lcd.print(String(maxPeople) + " / " + String(maxPeople));
        }

        if (currentPeople == maxPeople) {
            digitalWrite(ledPin, HIGH);
        } else if(currentPeople > maxPeople) {
            digitalWrite(buzzerPin, HIGH);
            delay(1000);
            digitalWrite(buzzerPin, LOW);
        } else {
            digitalWrite(ledPin, LOW);
            digitalWrite(buzzerPin, LOW);
        }

        delay(1000);
    }
}
