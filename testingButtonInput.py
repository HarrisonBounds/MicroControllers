#Harrison Bounds
#Testing button input

#Import libraries
import RPi.GPIO as GPIO
import time

#Tell the pi to use the GPIO number
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN)

counter = 0

while True:
    input_value = GPIO.input(40) #Setting the input from pin 21 to the variable input_value
    
    if input_value == False:
        counter = counter + 1
        
        print("The button has been pushed ", counter, " times!")
        
        #wait 250ms for the button bounce
    time.sleep(0.20)
    

