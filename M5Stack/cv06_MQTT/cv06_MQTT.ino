#include <M5Core2.h>
#include <WiFi.h>
#include <MQTT.h>

WiFiClient net;
MQTTClient client;

void messageReceived(String &topic, String &payload) {
  M5.Lcd.clear();
  M5.Lcd.setCursor(0,0);
  M5.Lcd.print("recv: " + topic + ": " + payload);
}


void setup() {
  Serial.begin(115200);
  M5.Lcd.begin(); 
  WiFi.begin("zpikiv", "78086975");
  
  while(!WiFi.isConnected()){
    Serial.print(".");
  }
    Serial.println("Wifi connected.");

  client.begin("test.mosquitto.org", net);
  client.onMessage(messageReceived);
  client.subscribe("/zpitest");
  client.setWill("/zpistatus", "offline");
  client.connect("M5ID");

  while(!client.connected()){
    Serial.print(".");
  }
    Serial.println("MQTT connected.");
}

void loop() {
  client.loop();
  client.publish("/zpitest", "hello", true, 0);
  delay(1000);

  //client.disconnect();
}