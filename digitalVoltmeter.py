#Harrison Bounds
#Activity 7 - Introduction to ADC0831 (Analog to Digital Converter)

import RPi.GPIO as GPIO
import time

#set Pins
CS = 5
CLK = 6
DO = 13
Y_LED = 17

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DO, GPIO.IN)
GPIO.setup(Y_LED, GPIO.OUT)

#Set bit counter
n = 0

#Convert to voltage
def int_to_voltage(int_equiv):
    voltage = int_equiv* 0.02
    return round(voltage, 2)

#Reading the measured digital value
def read_digital_value(d):
    
        #Read data synched to clock pulses
        for n in range(0, 8): #8-bits
            GPIO.output(CLK, False)
            time.sleep(0.0001)
            
            GPIO.output(CLK, True)
            time.sleep(0.0001)
            
            GPIO.output(CLK, False)
            time.sleep(0.0001)
            
            #Listen to the DO pin for a bit(value)
            DO_State = GPIO.input(DO)
            if DO_State == True:
                d = d + "1"
            else:
                d = d + "0"
        return d

#Check to see if the voltage is outside of the specified range
def warning_check(voltage):
    if voltage < 1 or voltage > 2:
        GPIO.output(Y_LED, True)
        time.sleep(0.3)
        GPIO.output(Y_LED, False)
        time.sleep(0.3)
    else:
        GPIO.output(Y_LED, False)

try:
    #Keep looking to read the voltage
    while True:
        #Set initial binary string to empty
        d = ""
        #Start with the CS pin to low
        GPIO.output(CS, False)
        time.sleep(0.0001)
        
        #We need to get the process started to talk the chip
        #cycling the clock on and off
        GPIO.output(CLK, False)
        time.sleep(0.0001)
        
        GPIO.output(CLK, True)
        time.sleep(0.0001)
        
        GPIO.output(CLK, False)
        time.sleep(0.0001)
        
        d = read_digital_value(d)
        
        #Display the binary number and the integer equivalent
        int_equiv = int(d, 2)
        print("The binary number is: " + d)
        print("The integer equivalent is: ", int_equiv)
        voltage = int_to_voltage(int_equiv)
        print("The voltage is: ", voltage)
        
        warning_check(voltage)
        
        time.sleep(0.5)
        
        #set CS pin to high to end the conversation
        GPIO.output(CS, True)
        
except KeyboardInterrupt:
    print("GAME OVER")
    
finally:
    GPIO.cleanup()
        