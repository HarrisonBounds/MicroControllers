#Harrison Bounds
#Exam 2 Part 2 - 3-Bit Rotary Encoder

import RPi.GPIO as GPIO
import time

contact1_pin = 26
contact2_pin = 19
contact3_pin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(contact1_pin, GPIO.IN)
GPIO.setup(contact2_pin, GPIO.IN)
GPIO.setup(contact3_pin, GPIO.IN)

try:
    while True:
        
        contact1 = GPIO.input(contact1_pin)
        contact2 = GPIO.input(contact2_pin)
        contact3 = GPIO.input(contact3_pin)
        
        if contact1 == 0 and contact2 == 0 and contact3 == 0:
            print("The angle is 0 to 45 degrees")
        elif contact1 == 0 and contact2 == 0 and contact3 == 1:
            print("The angle is 45 to 90 degrees")
        elif contact1 == 0 and contact2 == 1 and contact3 == 1:
            print("The angle is 90 to 135 degrees")
        elif contact1 == 0 and contact2 == 1 and contact3 == 0:
            print("The angle is 135 to 180 degrees")
        elif contact1 == 1 and contact2 == 1 and contact3 == 0:
            print("The angle is 180 to 225 degrees")
        elif contact1 == 1 and contact2 == 1 and contact3 == 1:
            print("The angle is 225 to 270 degrees")
        elif contact1 == 1 and contact2 == 0 and contact3 == 1:
            print("The angle is 270 to 315 degrees")
        elif contact1 == 1 and contact2 == 0 and contact3 == 0:
            print("The angle is 315 to 360 degrees")
            
        time.sleep(1)

except KeyboardInterrupt:
    print("Goodbye!")
    
finally:
    GPIO.cleanup()
            
            
            
            
            
            
            
            
            
            
            
            