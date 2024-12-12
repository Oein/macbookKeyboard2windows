#include <Wire.h>

void setup()
{
  Wire.begin(); // join i2c bus (address optional for master)
  Serial.begin(115200);
}

void loop()
{
  int avaBytes = Serial.available();
  if(avaBytes) {
    Wire.beginTransmission(4);
    while(avaBytes--) {
      char serialRead = Serial.read();
      Wire.write(serialRead);
    }
    Wire.endTransmission();
  }
}
