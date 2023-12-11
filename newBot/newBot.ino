#include <DHT.h>
#include <ESP8266WiFi.h>

const char *ssid = "ba-wifi";
const char *password = "1peter4:10";
const char *token = "6817021114:AAFDrDSYzCT9OMjlbDg7iIk0c2R6UH7KFcU";

const int DHT_PIN = 13; // DHT11 data pin
const int PIR_PIN = 14; // PIR motion sensor pin

DHT dht(DHT_PIN, DHT11);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(250);
        Serial.print(".");
    }
    Serial.println("WiFi connected");
}

void loop() {
    float temperature = dht.readTemperature();
    int motion = digitalRead(PIR_PIN);

    if (!isnan(temperature) && motion == HIGH) {
        sendTelegramMessage(temperature);
        delay(60000); // Send only one message per minute to avoid flooding
    }

    delay(1000);
}

void sendTelegramMessage(float temperature) {
    WiFiClientSecure client;
    if (client.connect("api.telegram.org", 443)) {
        String url = "/bot" + String(token) + "/sendMessage?chat_id=@YourChannelID&text=Temperature: " + String(temperature) + "C";
        client.print(String("GET ") + url + " HTTP/1.1\r\n" +
                     "Host: api.telegram.org\r\n" +
                     "Connection: close\r\n\r\n");
        while (client.connected()) {
            if (client.available()) {
                String line = client.readStringUntil('\r');
                Serial.print(line);
            }
        }
        client.stop();
    }
}
