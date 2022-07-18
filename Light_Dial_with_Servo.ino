//Program that moves servo arm depending on how light/dark it is. Dark closer to 0, light closer to 180
#include <Servo.h>

int lightPin = A0;
int servoPin = 9;
int lightVal;
int angle;

Servo myServo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(lightPin, INPUT);
  pinMode(servoPin, OUTPUT);
  myServo.attach(servoPin);

}

void loop() {
  // put your main code here, to run repeatedly:
lightVal = analogRead(lightPin);
Serial.println(lightVal);
delay(700);

angle = (-17.0/52) * lightVal + (17.0 * 550 / 52.0); //Equation I worked out on paper



myServo.write(angle);



}
