#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE

#include <DabbleESP32.h>
#include <M5Core2.h>

// the setup function runs once when you press reset or power the board
void setup() {
	Serial.begin(9600);
  M5.Lcd.begin();
  Serial.println("Init.");

	Dabble.begin("MyEsp32");
  Serial.println("Dabble Init.");
}

	// the loop function runs over and over again until power down or reset
	void loop() {
	Dabble.processInput();
	Serial.println(GamePad.getx_axis());
	Serial.println(GamePad.getYaxisData());
	Serial.println();

  M5.Lcd.clear();
  M5.Lcd.setCursor(0,0);
  M5.Lcd.print(GamePad.getx_axis());

  delay(100);
}