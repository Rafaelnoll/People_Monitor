int LED = 8;

void setup(){
    Serial.begin(115280);
    pinMode(LED, OUTPUT);

    while(!Serial){};
}

void loop(){
    String message = Serial.readString();

    if(message == "ON"){
        digitalWrite(LED, HIGH);
        Serial.println("LIGADO");
    } else if(message == "OFF") { 
        digitalWrite(LED, LOW);
        Serial.println("DESLIGADO");
    }

}