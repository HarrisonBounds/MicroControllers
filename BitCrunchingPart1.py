#Bit Crunching Part 1

import RPi.GPIO as GPIO
import time

#set pins
button_1 = 17
button_2 = 22
button_3 = 27
led_1 = 18
led_2 = 19
led_3 = 12

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(button_2, GPIO.IN)
GPIO.setup(button_3, GPIO.IN)

GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)

#Need to start with the LEDs off
GPIO.output(led_1, False)
GPIO.output(led_2, False)
GPIO.output(led_3, False)

try:
    repeat = True
    while repeat == True:
        button_1_state = GPIO.input(button_1) # read the state of button 1 (HIGH or LOW?)
        button_2_state = GPIO.input(button_2) #read the state of button 2
        button_3_state = GPIO.input(button_3)
        
        #Set the LED states to match the button states
        GPIO.output(led_1, button_1_state)
        GPIO.output(led_2, button_2_state)
        GPIO.output(led_3, button_3_state)
        
        #Compute the integer equivalent of the binary input
        d = (3 * button_1_state) + (2 * button_2_state) + (1 * button_3_state)
        
        #Clear the screen
        time.sleep(0.5)
        
        #Display the information to the user
        print("The state of button 1 is: ", button_1_state)
        print("The state of button 2 is: ", button_2_state)
        print("The state of button 3 is: ", button_3_state)
        print("3-bit binary number:")
        
        print("button 1: ", bin(button_1_state))
        print("button 2: ", bin(button_2_state))
        print("button 2: ", bin(button_3_state))
        
        print("Integer Equivalent: ", d)
        print("\n")
        
        repeat_str = input("Play again? Y or N: ")
        if repeat_str == "N":
            repeat = False
            
            print("Thanks for playing... Goodbye!")
        else:
            repeat = True

except KeyboardInterrupt:
    print("You sunk my battleship!")
    
finally:
    GPIO.cleanup()
    
        
        
        
        
        
        
        
        
        
        
