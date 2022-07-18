int lightPin = A0;
int greenPin = 13;
int redPin = 2;
int lightVal;

void setup() {
  // put your setup code here, to run once:
pinMode(lightPin, INPUT);
pinMode(greenPin, OUTPUT);
pinMode(redPin, OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
lightVal = analogRead(lightPin);

Serial.println(lightVal);
delay(1000); 

if(lightVal > 100)
{
  digitalWrite(greenPin, HIGH);
  digitalWrite(redPin, LOW);
}
else
{
  digitalWrite(redPin, HIGH);
  digitalWrite(greenPin, LOW);
}
}
