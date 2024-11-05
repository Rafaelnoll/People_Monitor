// Programa: Display LCD 16x2 e módulo I2C
// Autor: Arduino e Cia

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Inicializa o display no endereço 0x27
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    Serial.begin(9600);  // Corrigido para uma taxa de baud comum
    lcd.init();          // Inicializa o LCD
    lcd.backlight();     // Ativa o backlight

    while (!Serial) {};  // Espera até o monitor serial estar disponível
}

void loop() {
    if (Serial.available() > 0) {  // Verifica se há dados no serial
        String message = Serial.readString();  // Lê a mensagem da Serial
        lcd.clear();                // Limpa o display
        lcd.setCursor(0, 0);        // Posiciona o cursor no início
        lcd.print(message);         // Imprime a mensagem no LCD
        delay(1000);                // Mantém a mensagem por 2 segundos
    }
}
