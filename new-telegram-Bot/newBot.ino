#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include <DHT.h>

const char* ssid = "REPLACE_WITH_YOUR_SSID";
const char* password = "REPLACE_WITH_YOUR_PASSWORD";

#define BOTtoken "6817021114:AAFDrDSYzCT9OMjlbDg7iIk0c2R6UH7KFcU"  // your Bot Token (Get from Botfather)
#define CHAT_ID "395826160"

X509List cert(TELEGRAM_CERTIFICATE_ROOT);
WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

const int motionSensor = 14;  // PIR Motion Sensor
const int dhtPin = 12;        // DHT11 Data pin
bool motionDetected = false;
unsigned long lastUpdateTime = 0;
const unsigned long updateInterval = 60000;  // 1 minute in milliseconds

DHT dht(dhtPin, DHT11);

void ICACHE_RAM_ATTR detectsMovement() {
  motionDetected = true;
}

void sendStatus() {
  float temperature = dht.readTemperature();
  // Check if the temperature is a valid value
  if (!isnan(temperature)) {
    String statusMessage = "Motion: " + String(motionDetected ? "Detected" : "Not Detected") +
                           "\nTemperature: " + String(temperature) + "°C";
    bot.sendMessage(CHAT_ID, statusMessage, "");
  } else {
    bot.sendMessage(CHAT_ID, "Motion: " + String(motionDetected ? "Detected" : "Not Detected") +
                             "\nTemperature: Not Available", "");
  
}

void handleMessages() {
  int numNewMessages = bot.getUpdates(bot.last_message_received + 1);
  while (numNewMessages) {
    for (int i = 0; i < numNewMessages; i++) {
      String chat_id = String(bot.messages[i].chat_id);
      String text = bot.messages[i].text;

      if (text == "/start") {
        bot.sendMessage(chat_id, "Hello! I am your motion and temperature bot. Use /status to get updates.");
      } else if (text == "/status") {
        sendStatus();
      }

      numNewMessages--;
    }
  }
}

void setup() {
  Serial.begin(115200);
  configTime(0, 0, "pool.ntp.org");
  client.setTrustAnchors(&cert);

  pinMode(motionSensor, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(motionSensor), detectsMovement, RISING);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  dht.begin();

  bot.sendMessage(CHAT_ID, "Bot started up", "");
}

void loop() {
  handleMessages();
  unsigned long currentMillis = millis();

  if (currentMillis - lastUpdateTime >= updateInterval) {
    sendStatus();
    lastUpdateTime = currentMillis;
  }

  if (motionDetected) {
    motionDetected = false;  // Reset the flag
  }
}
