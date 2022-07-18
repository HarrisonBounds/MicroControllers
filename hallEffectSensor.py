#Hall Effect Sensor to detect a south magnetic pole

import RPi.GPIO as GPIO
import time

#Set GPIO pin
HES = 26 #Hall Effect Sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(HES, GPIO.IN)

try:
    count = 0
    run_time = 10
    start_time = time.time()
    repeat = True
    
    while time.time() - start_time < run_time:
        #check the state of the HES
        HES_state = GPIO.input(HES)
        
        while HES_state == True and time.time() - start_time < run_time:
            print("Nothing detected")
            HES_state = GPIO.input(HES)
            
            
        while HES_state == False and time.time() - start_time < run_time: 
            print("South Magnetic Pole Detected!")
            HES_state = GPIO.input(HES)
            
        
        
        count = count + 1
        print("The pole has detected the sensor ", count, " times!*")
        
        
        
    print("The rpm is ", count * 60/11, "rpm")
        
except KeyboardInterrupt:
    print("That's all folks!")
    
finally:
    GPIO.cleanup()