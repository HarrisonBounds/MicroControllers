#Harrison Bounds
#Lab Report 1
#Blinky Led with button rate

import RPi.GPIO as GPIO
import time

#Set pins
button1_pin = 17
button2_pin = 22
blue_LED = 21


def button1_handler(pin):
    global rate
    time.sleep(0.01)
    rate = rate - 0.1
    print("Flashing rate decreased!")
    
def button2_handler(pin):
    global rate
    time.sleep(0.01)
    rate = rate + 0.1
    print("Flashing rate increased!")

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(blue_LED, GPIO.OUT)
GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback = button1_handler, bouncetime = 300)
GPIO.add_event_detect(button2_pin, GPIO.BOTH, callback = button2_handler, bouncetime = 300)

#Start with the led off
GPIO.output(blue_LED, False)

#Start with the rate at 1 second
rate = 1

try:
    while True:
        GPIO.output(blue_LED, True)
        time.sleep(rate)
        GPIO.output(blue_LED, False)
        time.sleep(rate)
        
except KeyboardInterrupt:
    print("Goodbye!!")

finally:
    GPIO.cleanup()
    
    

        
        
    
    