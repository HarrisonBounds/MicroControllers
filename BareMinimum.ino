int voltPin = A2;
int readValue;
double V2;
int wait = 1000;
int redPin = 9;

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200); //Make sure baud in serial monitor is this same value
pinMode(redPin, INPUT);
pinMode(redPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
readValue = analogRead(voltPin);
//Convert to voltage
V2 = (5.0 / 1023.0) * readValue;
Serial.println(V2);

if (V2 > 2.5 && V2 < 4.0)
{
  digitalWrite(redPin, HIGH);
}
if (V2 < 2.5 || V2 > 4)
{
  digitalWrite(redPin, LOW);
}

delay(wait);

}
