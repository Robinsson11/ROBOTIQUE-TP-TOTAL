
#include <SoftwareSerial.h>
SoftwareSerial mySerial(2, 3); // RX, TX
SoftwareSerial mySerial2(5, 6); // RX, TX

void setup() {
    Serial.begin(38400);
    mySerial2.begin(38400);
    mySerial.begin(38400);
}

void loop() {
  if (Serial.available()) {      // If anything comes in Serial (USB),
    mySerial.write(Serial.read());   // read it and send it out Serial1 (pins 0 & 1)
  }
  
  if (mySerial2.available()) {      // If anything comes in Serial (USB),
    mySerial.write(mySerial2.read());   // read it and send it out Serial1 (pins 0 & 1)
  }

  if (mySerial.available()) {     // If anything comes in Serial1 (pins 0 & 1)
    Serial.write(mySerial.read());   // read it and send it out Serial (USB)
  }
}
