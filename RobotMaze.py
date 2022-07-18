#Harrison Bounds
#Robot Through a Maze!
import RPi.GPIO as GPIO
import time

#set GPIO pin
left_servo = 26
right_servo = 19
button_pin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_servo, GPIO.OUT)
GPIO.setup(right_servo, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

#define the function to turn clockwise
def turn_servo(pulse_duration_left, pulse_duration_right, delta_t):
    #pulse_duration = 1.7 * 10 ** (-3) #seconds, max value for CW rotation
    sleep_time = 20 * 10 ** (-3) # seconds, 20ms required
    start_time = time.time()
    
    left_state = True
    right_state = True
    
    if pulse_duration_left == 0:
        left_state = False
        
    if pulse_duration_right == 0:
        right_state = False
    
    while time.time() - start_time < delta_t:
        GPIO.output(left_servo, left_state)
        time.sleep(pulse_duration_left)
        
        GPIO.output(right_servo, right_state)
        time.sleep(pulse_duration_right)
        
        GPIO.output(left_servo, False)
        GPIO.output(right_servo, False)
        time.sleep(sleep_time)
        #pulse_duration = pulse_duration + (0.04 * 10 ** (-3))
    
    GPIO.output(left_servo, False)
    GPIO.output(right_servo, False)
    return

try:
    while True:
        button_input = GPIO.input(button_pin)
        
        if button_input == False:
        
            '''turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 3.2)
            time.sleep(0.25)
            
            turn_servo(0, 1.3 * 10 ** (-3), 1) #Turn Left
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 0.5)
            time.sleep(0.25)
            
            turn_servo(0, 1.3 * 10 ** (-3), 0.5) #Turn Left
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 0.25)
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 0, 0.5) #Turn Right
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 0.4)
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 0, 0.5) #Turn Right
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 0.3)
            time.sleep(0.25)
            
            turn_servo(0, 1.3 * 10 ** (-3), 0.5) #Turn Left
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 4)
            time.sleep(0.25)
            
            turn_servo(0, 1.3 * 10 ** (-3), 1) #Turn Left
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 3)
            time.sleep(0.25)'''
           
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 0.5)
            time.sleep(0.25)
            
            turn_servo(0, 1.3 * 10 ** (-3), 0.6) #Turn Left
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 6)
            time.sleep(0.25)
            
            turn_servo(0, 1.3 * 10 ** (-3), 1) #Turn Left
            time.sleep(0.25)
            
            turn_servo(1.7 * 10 ** (-3), 1.3 * 10 ** (-3), 2)
            time.sleep(0.25)
   
        
except KeyboardInterrupt:
    print("Im sorry... Goodbye")
    
finally:
    GPIO.cleanup()
        