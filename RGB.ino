int red = 8;
int green = 9;
int blue = 10;
String color;
String msg = "What color do you want?: ";

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(red, OUTPUT);
pinMode(green, OUTPUT);
pinMode(blue, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println(msg);
while (Serial.available() == 0)
{
}

color = Serial.readString();

if (color == "red")
{
  digitalWrite(red, HIGH);
  digitalWrite(green, LOW);
  digitalWrite(blue, LOW);
}

if (color == "green")
{
  digitalWrite(green, HIGH);
  digitalWrite(red, LOW);
  digitalWrite(blue, LOW);
}

if (color == "blue")
{
  digitalWrite(blue, HIGH);
  digitalWrite(red, LOW);
  digitalWrite(green, LOW);
}

if (color == "off")
{
  digitalWrite(blue, LOW);
  digitalWrite(red, LOW);
  digitalWrite(green, LOW);
}

if (color == "purple")
{
  analogWrite(blue, 200);
  analogWrite(red, 200);
  digitalWrite(green, LOW);
}

}
