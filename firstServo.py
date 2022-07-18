#Continous rotation servo

import RPi.GPIO as GPIO
import time

#set GPIO pin
servo_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

#define the function to turn clockwise
def turn_servo(pulse_duration, delta_t):
    #pulse_duration = 1.7 * 10 ** (-3) #seconds, max value for CW rotation
    sleep_time = 20 * 10 ** (-3) # seconds, 20ms required
    start_time = time.time()
    
    while time.time() - start_time < delta_t:
        GPIO.output(servo_pin, True)
        time.sleep(pulse_duration)
        GPIO.output(servo_pin, False)
        time.sleep(sleep_time)
        pulse_duration = pulse_duration + (0.04 * 10 ** (-3))
    
    print(pulse_duration)
    
    GPIO.output(servo_pin, False)
    return

try:
    #while True:
        #turn clockwise for 3 seconds
        #pulse_duration_str = input("input pulse duration in milliseconds: ")
        #pulse_duration = float(pulse_duration_str)
        
        
        
    turn_servo(1.5 * 10 ** (-3), 5)
        
except KeyboardInterrupt:
    print("Im sorry... Goodbye")
    
finally:
    GPIO.cleanup()
        
        
        
        
        
        
        
        
        