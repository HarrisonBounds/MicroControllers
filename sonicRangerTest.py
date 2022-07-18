#Harrison Bounds
#Ultrasonic sensor

import RPi.GPIO as GPIO
import time
from numpy import sqrt

GPIO.setmode(GPIO.BCM)

pin = 26


def ReadDistance(pin):
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False) #set pin low
    time.sleep(2 * 10 **(-6)) #sleep for two microseconds
    
    #send trigger signal
    GPIO.output(pin, True)
    time.sleep(5 * 10 **(-6)) #sleep for five microseconds
    GPIO.output(pin, False)
    
    #setup the pin as an input to watch for an echo
    GPIO.setup(pin, GPIO.IN)
    
    #after output signal, the PING sensor returns to a logical high until it detects the echo
    while GPIO.input(pin) == False: #catches the last instant the pin was low
        start_time = time.time()
        
    while GPIO.input(pin) == True: #catches the last instant the pin was high
        end_time = time.time()
        
    duration = end_time - start_time #time of flight for the sound
    
    #distance is defined as time / 2 (There and back / 2) * speed of sound(34000cm/s)
    distance = (duration * 34000) / 2
    
    return distance


try:
    distance_array = []
    
    while True:
        distance = ReadDistance(pin)
        distance_array.append(distance)
        
        print("Distance (cm) to object is ", round(distance, 2))
        time.sleep(1)
        
        
except KeyboardInterrupt:
    print("AWWWWW shucks")
    
finally:
    GPIO.cleanup()