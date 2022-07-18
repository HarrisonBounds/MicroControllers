int xPin = A0;
int yPin = A1;
int switchPin = 8; //B on Joystick (Stands for Button?)

int xVal;
int yVal;
int switchVal;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(xPin, INPUT);
pinMode(yPin, INPUT);
pinMode(switchPin, INPUT); //do a digital read to read a 1 or 0 from this
digitalWrite(switchPin, HIGH);


}

void loop() {
  // put your main code here, to run repeatedly:
xVal = analogRead(xPin); //Analog reads read a value from 0 to 1023
yVal = analogRead(yPin);
switchVal = digitalRead(switchPin); //digital Read reads a value that is either 0 or 1

delay(500);

Serial.print("X Value: ");
Serial.print(xVal);
Serial.print("  Y Value: ");
Serial.print(yVal);
Serial.print("  Switch State: ");
Serial.println(switchVal);



}
