#Harrison Bounds
#Blinky LED

#Import libraries
import RPi.GPIO as GPIO
import time

#Tell the pi to use the GPIO number and use pin 21 as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

#rate = float(input("What do you want the blink rate to be?: "))
rate = 1

while True:
        i = 0
        j = 0
        
        while i < 9:    
            GPIO.output(21, True) #True means high
            GPIO.output(17, False)
            
            time.sleep(rate)
            
            GPIO.output(17, True)
            GPIO.output(21, False)
            
            time.sleep(rate)
            
            rate = rate - 0.10 #Iterator for the rate
            i = i + 1 #Iterator for the loop when slowing down
        
        while j < 9:
            
            GPIO.output(21, True) #True means high
            GPIO.output(17, False)
            
            time.sleep(rate)
            
            GPIO.output(17, True)
            GPIO.output(21, False)
            
            time.sleep(rate)
            
            rate = rate + 0.10 #Iterator for the rate
            j = j + 1 #Iterator for the loop when speeding up
    
    



