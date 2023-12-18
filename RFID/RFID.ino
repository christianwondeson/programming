#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance

// Maximum number of allowed registered cards
const int maxRegisteredCards = 4;

// Valid UIDs of registered cars
byte validUIDs[maxRegisteredCards][4] = {
  {0, 0, 0, 0},
  {0, 0, 0, 0},
  {0, 0, 0, 0},
  {0, 0, 0, 0},
};

// car brands
const char*   carNames[] = {
  "TOYOTA VAN",  // Name of car 1
  "HIGH ROOF",    // Name of car 2
  "DAMAS",       // Name of car 3
  " SUZUKI",     // Name of car 4
};

// LCD I2C display
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Adjust the address and size according to your display

void setup() {
  Serial.begin(9600);   // Initialize serial communication
  SPI.begin();          // Initiate SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  lcd.begin(16, 2);     // Initialize the LCD display
  lcd.init();
  lcd.backlight();      // Turn on the backlight
  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("Scan ID card");
  Serial.println("Ready to read RFID cards");
}

void loop() {
  // Look for new cards
  if (mfrc522.PICC_IsNewCardPresent()) {
    if (mfrc522.PICC_ReadCardSerial()) {
      // Show UID on serial monitor
      Serial.print("UID tag: ");
      for (byte i = 0; i < mfrc522.uid.size; i++) {
        Serial.print("0x");
        if (mfrc522.uid.uidByte[i] < 0x10) Serial.print("0");
        Serial.print(mfrc522.uid.uidByte[i], HEX);
        if (i < mfrc522.uid.size - 1) Serial.print(", ");
      }
      Serial.println();
      Serial.print("UID Number: ");
      String content = "";
      byte letter;
      for (byte i = 0; i < mfrc522.uid.size; i++) {
        content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
        content.concat(String(mfrc522.uid.uidByte[i], HEX));
      }
      content.toUpperCase();
      Serial.println(content);

      // Check if the UID is already registered
      int carIndex = findRegisteredCard(content);

      // Perform actions based on registration status
      if (carIndex == -1) {
        // Card is not registered, perform registration

        // Find an empty slot for registration
        carIndex = findEmptySlot();
        if (carIndex != -1) {
          // Update the registered card information
          memcpy(validUIDs[carIndex], mfrc522.uid.uidByte, mfrc522.uid.size);

          // Display registration success on the LCD
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("Registered:");
          lcd.setCursor(0, 1);
          lcd.print(carNames[carIndex]);
          delay(3000);  // Display registration success for 3 seconds
        } else {
          // No empty slot available for registration, display message
          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print("Max cards reached");
          lcd.setCursor(0, 1);
          lcd.print("Cannot register");
          delay(2000);
        }
      } else {
        // Card is already registered, display message
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Card already");
        lcd.setCursor(0, 1);
        lcd.print("registered");
        delay(2000);
      }

      // Clear the LCD display and reset for the next scan
      lcd.clear();
      lcd.setCursor(2, 0);
      lcd.print("Scan ID card");

      delay(1000);   // Delay to avoid reading the card multiple times in a short period
    }
    mfrc522.PICC_HaltA();   // Stop reading
    mfrc522.PCD_StopCrypto1();  // Stop encryption on PCD
  }
}

// Function to find the index of a registered card based on UID
int findRegisteredCard(String uid) {
  for (int i = 0; i < maxRegisteredCards; i++) {
    String registeredUID = "";
    for (int j = 0; j < mfrc522.uid.size; j++) {
      registeredUID += (validUIDs[i][j] < 0x10 ? "0" : "");
      registeredUID += String(validUIDs[i][j], HEX);
    }
    registeredUID.toUpperCase();

    if (uid == registeredUID) {
      return i;  // Card is already registered, return index
    }
  }
  return -1;  // Card is not registered
}

// Function to find an empty slot for registration
int findEmptySlot() {
  for (int i = 0; i < maxRegisteredCards; i++) {
    if (validUIDs[i][0] == 0 && validUIDs[i][1] == 0 && validUIDs[i][2] == 0 && validUIDs[i][3] == 0) {
      return i;  // Empty slot found, return index
    }
  }
  return -1;  // No empty slot available
}
