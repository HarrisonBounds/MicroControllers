#Harrison Bounds
#LED Pulse Width Modulation

import RPi.GPIO as GPIO
import time

#set GPIO Pin
LED = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

#set up the LED as a PWM object
freq = 100 #Hertz
my_pwm = GPIO.PWM(LED, freq)

#start the led object
duty_cycle = 0 #percentage, 0% = OFF, 100% = fully ON
my_pwm.start(duty_cycle)

pause_time = 1 #seconds

try:
    while True:
        duty_cycle = 100 #start at 100%
        wait = 3 #wait time for the duty cycle to go from 100 to 0 (seconds)
        
        #prompt user for a duty cycle input
        #duty_cycle_string = input("Input duty cycle as percentage: ")
        #duty_cycle = int(duty_cycle_string) #converts string to integer
        #print("The duty cycle is: ", duty_cycle)
        start_time = time.time()
        
        while time.time() - start_time < wait:
            duty_cycle = duty_cycle - 12
            my_pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.4)
            
        start_time2 = time.time()
            
        while time.time() - start_time2 < wait:
            duty_cycle = duty_cycle + 12
            my_pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.4)
            
        
        time.sleep(pause_time)
        
except KeyboardInterrupt:
    my_pwm.stop() #This stops the PWM object
    print("Thats all folks")
    
finally:
    GPIO.cleanup()
        