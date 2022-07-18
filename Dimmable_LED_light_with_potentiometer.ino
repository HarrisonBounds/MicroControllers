int readPin = A2;
int redPin = 6;
int readVal; //# between 0 and 1023 (Will convert later)
double LEDVal;


void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(redPin, OUTPUT);
pinMode(readPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
readVal = analogRead(readPin);       //reading the potentiometer value and then 
                                     //assigning it to the readVal variable

LEDVal = (255.0 / 1023.0) * readVal; //Here we converted the potentiometer
                                     //to an RGB vaue for the LED pin
                                     
analogWrite(redPin, LEDVal);         //TWO PARAMETERS: 1st is which pin you use
                                     //2nd is what value you want to use (0 - 255)
                                     
Serial.println(LEDVal);              //Prints the values on the serial monitor


}
