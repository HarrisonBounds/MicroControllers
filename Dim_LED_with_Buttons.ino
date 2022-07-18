int buttonUp = 5;
int buttonDown = 6;
int LEDpin = 3;
int upRead;
int downRead;
int LEDbright = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(LEDpin, OUTPUT);
pinMode(buttonUp, INPUT);
pinMode(buttonDown, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  upRead = digitalRead(buttonUp);
  downRead = digitalRead(buttonDown);

  Serial.print("Button 1: ");
  Serial.print(upRead);
  Serial.print(", ");

  Serial.print("Button 2: ");
  Serial.println(downRead);

  if(upRead == 0)
  {
    LEDbright = LEDbright + 1;
     
  }

  if(downRead == 0)
  {
    LEDbright = LEDbright - 1;
  }

  if(LEDbright > 255)
  {
    LEDbright = 255;
  }
  
  if(LEDbright < 0)
  {
    LEDbright = 0;
  }

  analogWrite(LEDpin, LEDbright);


}
