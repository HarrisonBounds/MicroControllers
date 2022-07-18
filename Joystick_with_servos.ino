#include<Servo.h>

Servo xServo; //Create the servo object
Servo yServo;

int xPin = A0;
int yPin = A1;
int xServoPin = 5;
int yServoPin = 3;
int switchPin = 8; //B on Joystick (Stands for Button?)
int angleX;
int angleY;
int xVal;
int yVal;
int switchVal;
int buzzPin = 11;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(xPin, INPUT);
pinMode(yPin, INPUT);
pinMode(switchPin, INPUT); //do a digital read to read a 1 or 0 from this
digitalWrite(switchPin, HIGH);

pinMode(xServoPin, OUTPUT);
pinMode(yServoPin, OUTPUT);

xServo.attach(xServoPin);
yServo.attach(yServoPin);

pinMode(buzzPin, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
xVal = analogRead(xPin); //Analog reads read a value from 0 to 1023
angleX = (180.0/1023) * xVal;

yVal = analogRead(yPin);
angleY = (180.0/1023) * yVal;

switchVal = digitalRead(switchPin); //digital Read reads a value that is either 0 or 1

xServo.write(angleX);
yServo.write(angleY);

if(switchVal == 1)
{
  digitalWrite(buzzPin, HIGH);
}
else
{
  digitalWrite(buzzPin, LOW);
}


Serial.print("X Value: ");
Serial.print(xVal);
Serial.print("  Y Value: ");
Serial.print(yVal);
Serial.print("  Switch State: ");
Serial.println(switchVal);

}
