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

def calc_mean(distance_array):
    total = 0
    for i in range(0, len(distance_array)):
        total = total + distance_array[i]
        
    mean = total / 10
    
    return mean

def calc_standard_deviation(distance_array, mean):
    sd = sqrt((1 / (len(distance_array) - 1)) * summation(distance_array, mean))
    
    sd_mean = sd / sqrt(len(distance_array))
    
    return sd_mean
              
def summation(distance_array, mean):
    summ = 0
    for i in range(0, len(distance_array)):
        summ = summ + pow((distance_array[i] - mean), 2)
    return summ

try:
    distance_array = []
    n = 0
    while n < 10:
        distance = ReadDistance(pin)
        distance_array.append(distance)
        
        print("Distance (cm) to object is ", round(distance, 2))
        time.sleep(1)
        
        n = n + 1
        
    mean = calc_mean(distance_array)
    sd_mean = calc_standard_deviation(distance_array, mean)
    print("The mean of the distances are ", mean)
    print("The standard deviation of the mean is ", sd_mean)
        
except KeyboardInterrupt:
    print("AWWWWW shucks")
    
finally:
    GPIO.cleanup()
    
    
    
    