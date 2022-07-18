#Blinky Button

import RPi.GPIO as GPIO
import time

button1_pin = 17
button2_pin = 22
LED_pin = 21
my_counter = 0


def button_handler_decrease(pin):
    global rate
    time.sleep(0.01)
    rate = rate - 0.1
    
def button_handler_increase(pin):
    global rate
    time.sleep(0.01)
    rate = rate + 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback=button_handler_decrease, bouncetime=300)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button2_pin, GPIO.BOTH, callback=button_handler_increase, bouncetime=300)
GPIO.setup(LED_pin, GPIO.OUT)

led_state = False
GPIO.output(LED_pin, False)

rate = 1
while True:
    #input_value = GPIO.input(button_pin)
    
    GPIO.output(LED_pin, True)
    time.sleep(rate)
    GPIO.output(LED_pin, False)
    time.sleep(rate)
    
    print("The flashing rate is ", round(rate, 1))
    
    
    
    '''if input_value == False:
        my_counter = my_counter + 1
        print("The button has been pushed ", my_counter, " times!")
        rate = rate - 0.1
        
        time.sleep(0.25)
        
        
        
        if led_state == False:
            led_state = True
            GPIO.output(LED_pin, led_state)
        else:
            led_state = False
            GPIO.output(LED_pin, led_state)'''
            