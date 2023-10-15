#include <M5Core2.h>

const int buttonPin = 27;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int count = 0;

void setup() {
  M5.Lcd.begin(); 
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  int state = digitalRead(buttonPin);
    
  if(state == 1){
    count++;
  }

  // M5.Lcd.clear();
  // M5.Lcd.setCursor(0,0);
  // M5.Lcd.setCursorY(0);
  // M5.Lcd.print();
  Serial.print(state);
  Serial.print(" ");
  Serial.println(count);
}
