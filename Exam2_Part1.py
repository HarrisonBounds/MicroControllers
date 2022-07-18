#Exam 2, Part1
#Harrison Bounds
#Tell if the Incremental Encoder is turning Clockwise or Counterclockwise

import RPi.GPIO as GPIO
import time

outside_pin = 26
inside_pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(outside_pin, GPIO.IN)
GPIO.setup(inside_pin, GPIO.IN)

try:
    count = 0
    while True:
        #if pin is True, it is reading black
        outside1 = GPIO.input(outside_pin)
        inside1 = GPIO.input(inside_pin)
        
        time.sleep(0.1)
        
        outside2 = GPIO.input(outside_pin)
        inside1 = GPIO.input(inside_pin)
        
        if outside1 == 0 and inside1 == 0 and outside2 == 1 and inside2 == 0:
            print("Clockwise!")
        elif outside1 == 0 and inside1 == 0 and outside2 == 0 and inside2 == 1:
            print("Counter-clockwise!")
        elif outside1 == 1 and inside1 == 1 and outside2 == 0 and inside2 == 1:
            print("Clockwise!")
        elif outside1 == 1 and inside1 == 1 and outside2 == 1 and inside2 == 0:
            print("Counter-clockwise!")
            
            
except KeyboardInterrupt:
    print("Goodbye!")
finally:
    GPIO.cleanup()