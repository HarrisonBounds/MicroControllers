#Using Relay to turn on and off a lightbulb
#Harrison Bounds

import RPi.GPIO as GPIO
import time

A1 = 18
A2 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)

try:
    while True:
        control = input("Would you like the bulb to be on or off? <Type On or Off>: ")
        
        if control == "On":
            GPIO.output(A2, False)
            GPIO.output(A1, True)
            
        if control == "Off":
            GPIO.output(A1, False)
            GPIO.output(A2, True)
            
except KeyboardInterrupt:
    print("Goodbye")
    
finally:
    GPIO.cleanup()