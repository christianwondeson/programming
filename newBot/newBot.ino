#include <ESP8266WiFi.h>
#include <ArduinoTelegramBot.h>
#include <DHT.h>

// Replace with your network credentials
const char* ssid = "your-ssid";
const char* password = "your-password";

// Replace with your Telegram bot token
const char* botToken = "your-bot-token";

// Replace with your chat ID
const long chatId = your-chat-id;

// Replace with your DHT sensor pin
#define DHTPIN D4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

// Replace with your PIR motion sensor pin
#define PIR_PIN D5

bool motionDetected = false;

void setup() {
  Serial.begin(115200);
  delay(10);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize DHT sensor
  dht.begin();

  // Initialize PIR motion sensor
  pinMode(PIR_PIN, INPUT);

  // Initialize Telegram bot
  Bot.begin(botToken);
}

void loop() {
  // Check for motion
  if (digitalRead(PIR_PIN) == HIGH) {
    if (!motionDetected) {
      Bot.sendMessage(chatId, "Motion detected!");
      motionDetected = true;
    }
  } else {
    motionDetected = false;
  }

  // Read temperature and humidity
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Check if the readings are valid
  if (!isnan(temperature) && !isnan(humidity)) {
    // Send temperature and humidity to Telegram
    String message = "Temperature: " + String(temperature) + "°C\nHumidity: " + String(humidity) + "%";
    Bot.sendMessage(chatId, message);
  }

  delay(5000); // Delay for 5 seconds
}
