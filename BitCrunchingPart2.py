#Bit Crunching Part 2

import RPi.GPIO as GPIO
import time

#set pins
button_1 = 17
button_2 = 22

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_1, GPIO.IN)
GPIO.setup(button_2, GPIO.IN)

#Set initial binary string to empty
d = ""

#set bit counter
n = 0

try:
    #Explain directions to the user
    print("To input a bit: ")
    
    print("1. Press and hold the left button (PIN 17)")
    print("2. Press and hold the right button (PIN 27)")
    print("3. Release the left button ")
    print("4. Release the right button ")
    print("\n")
    
    #Number of bits 
    while n < 4:
        print("Waiting for user input...")
        
        #This tells Python to watch for a LOW --> HIGH signal
        GPIO.wait_for_edge(button_1, GPIO.RISING)
        time.sleep(0.3) #Compensate for button bounce
        
        GPIO.wait_for_edge(button_1, GPIO.FALLING)
        time.sleep(0.3)
        
        #Read the state of button 2
        button_2_state = GPIO.input(button_2)
        
        #Use the state of button 2 to append a bit to the binary string
        if button_2_state == True:     #if button 2 is pressed, the value is 1
            d = d + "1"
            
        else:
            d = d + "0"
            
        #Tell the user the bit they entered
        print("The bit you entered is: ", int(button_2_state))
        
        #Increment the bit counter
        n = n + 1
        
    #Tell the user the binary number and the integer equivalent
    print("The binary number is: " + d)
    print("The integer equivalent is: ", int(d, 2))
    print("\n")
    
except KeyboardInterrupt:
    print("Goodbye!")
    
finally:
    GPIO.cleanup()
    
        
        
        
        
        
        
        
        
        
        
    