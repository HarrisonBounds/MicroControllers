int buttonPin = 13;
int ledPin = 8;
int buttonRead;


void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ledPin, OUTPUT);
pinMode(buttonPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
buttonRead = digitalRead(buttonPin); // digital read returns 0 or 1

Serial.println(buttonRead);

if(buttonRead == 0)
{
  digitalWrite(ledPin, HIGH);
}
else
{
  digitalWrite(ledPin, LOW);
}
}
