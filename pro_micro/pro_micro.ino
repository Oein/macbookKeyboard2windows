#include <Wire.h>
#include <Keyboard.h>

int RXLED = 17;

void setup() {
  // Serial.begin(115200);
  pinMode(RXLED, OUTPUT);
  // put your setup code here, to run once:
  Wire.begin(4);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
}

void loop() {
  // put your main code here, to run repeatedly:
  
}

uint8_t keys[] = {
  '`',
  '1',
  '2',
  '3',
  '4',
  '5',
  '6',
  '7',
  '8',
  '9',
  '0',
  '-',
  '=',
  'q',
  'w',
  'e',
  'r',
  't',
  'y',
  'u',
  'i',
  'o',
  'p',
  '[',
  ']',
  '\\',
  'a',
  's',
  'd',
  'f',
  'g',
  'h',
  'j',
  'k',
  'l',
  ';',
  '\'',
  'z',
  'x',
  'c',
  'v',
  'b',
  'n',
  'm',
  ',',
  '.',
  '/',
  KEY_LEFT_ARROW,
  KEY_UP_ARROW,
  KEY_DOWN_ARROW,
  KEY_RIGHT_ARROW,
  KEY_TAB,
  KEY_LEFT_SHIFT,
  KEY_RIGHT_SHIFT,
  KEY_BACKSPACE,
  KEY_LEFT_CTRL,
  KEY_LEFT_ALT,
  KEY_LEFT_GUI,
  KEY_RIGHT_GUI,
  KEY_RIGHT_ALT,
  KEY_RIGHT_CTRL,
  KEY_ESC,
  KEY_CAPS_LOCK,
  KEY_F1,
  KEY_F2,
  KEY_F3,
  KEY_F4,
  KEY_F5,
  KEY_F6,
  KEY_F7,
  KEY_F8,
  KEY_F9,
  KEY_F10,
  KEY_F11,
  KEY_F12,
  KEY_RETURN,
  KEY_DELETE,
  KEY_PAGE_DOWN,
  KEY_PAGE_UP,
  ' ',
  KEY_HOME,
  KEY_END,
};

int dt(unsigned char data) {
  int x = 0;
  for(int i = 0;i < 7;i++) {
    if(data & (1 << i)) x |= (1 << i);
  }
  return x;
}

void printBinary(unsigned char value) {
  for (int i = 7; i >= 0; i--) {
    Serial.print((value >> i) & 1);
  }
  Serial.println();
}

void handleChar(unsigned char inp) {
  bool press = inp & (1 << 7);
  // printBinary(inp);
  int acs = dt(inp);
  if(acs > sizeof(keys)/sizeof(uint8_t)) return;
  // Serial.print(press?"Press " : "Release ");
  // Serial.println((int)keys[acs]);

  if(press) Keyboard.press(keys[acs]);
  else Keyboard.release(keys[acs]);
}

void receiveEvent(int howMany)
{
  while(Wire.available()) // loop through all but the last
  {
    digitalWrite(RXLED, LOW);
    handleChar(Wire.read());
  }

  digitalWrite(RXLED, HIGH);
}