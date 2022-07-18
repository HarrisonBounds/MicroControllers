#Harrison Bounds
#h-bridge

import RPi.GPIO as GPIO
import time

#Set GPIO pins
pin_EN = 26
pin_1A = 13
pin_2A = 19

run_time = 10 #seconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_EN, GPIO.OUT)
GPIO.setup(pin_1A, GPIO.OUT)
GPIO.setup(pin_2A, GPIO.OUT)

#set up pin1 as a PWM object
freq = 100 #Hertz
my_pwm = GPIO.PWM(pin_EN, freq)

duty_cycle = 0 #percentage: 0% = FULLY OFF : 100% = FULLY ON
my_pwm.start(duty_cycle)

try:
    GPIO.output(pin_EN, True)
    GPIO.output(pin_1A, True)
    GPIO.output(pin_2A, False)
    
    start_time = time.time()
    while time.time() - start_time < 30:
        duty_cycle = duty_cycle + 3
        my_pwm.ChangeDutyCycle(duty_cycle)
        print(duty_cycle)
        time.sleep(1)
        
    start_time = time.time()
    while time.time() - start_time < 10:
        duty_cycle = 100
        my_pwm.ChangeDutyCycle(duty_cycle)
        print(duty_cycle)
        time.sleep(1)
        
    start_time = time.time()
    while time.time() - start_time < 30:
        duty_cycle = duty_cycle - 3
        my_pwm.ChangeDutyCycle(duty_cycle)
        print(duty_cycle)
        time.sleep(1)
        
        
    GPIO.output(pin_EN, False)
    GPIO.output(pin_1A, False)
    GPIO.output(pin_2A, False)
        
    time.sleep(5)
        
    GPIO.output(pin_EN, True)
    GPIO.output(pin_1A, False)
    GPIO.output(pin_2A, True)
        
    start_time = time.time()
    while time.time() - start_time < 30:
        duty_cycle = duty_cycle + 3
        my_pwm.ChangeDutyCycle(duty_cycle)
        print(duty_cycle)
        time.sleep(1)
        
    start_time = time.time()
    while time.time() - start_time < 10:
        duty_cycle = 100
        my_pwm.ChangeDutyCycle(duty_cycle)
        print(duty_cycle)
        time.sleep(1)
        
    start_time = time.time()
    while time.time() - start_time < 30:
        duty_cycle = duty_cycle - 3
        my_pwm.ChangeDutyCycle(duty_cycle)
        print(duty_cycle)
        time.sleep(1)
    

        
    
        
        

except KeyboardInterrupt:
    print("Goodbye!")
    
finally:
    GPIO.cleanup()
        
    