int readPin = A2;
int readVal; // read between 0 and 1023 (Convert to 0 and 5 later)
int buzzPin = 8;
double convertVal;
int wait = 200;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(buzzPin, OUTPUT);
pinMode(readPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
readVal = analogRead(readPin);

convertVal = (5.0 / 1023.0) * readVal;

analogWrite(buzzPin, convertVal);

Serial.println(convertVal);
delay(wait); 

while (convertVal == 5)
{
  digitalWrite(buzzPin, HIGH);
  delay(500);
  Serial.println(convertVal);
  break;
}
digitalWrite(buzzPin, LOW);
}
