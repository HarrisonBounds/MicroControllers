#include <Servo.h> //Include library to work with servos

int servoPin = 9;
int servoPos = 170 ; //In degrees

Servo myServo; //Creating a servo object


void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
myServo.attach(servoPin); //Telling the arduino that the servo is attached to pin 9

}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println("What Angle for the Servo? "); //Prompting the angle for the servo
while(Serial.available() == 0)
{
  
}
servoPos = Serial.parseInt();

myServo.write(servoPos); // Telling the servo to go to the users specified degrees
}
