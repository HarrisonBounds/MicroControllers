#Using Relay to turn on and off a lightbulb
#Harrison Bounds

import RPi.GPIO as GPIO
import time

A1 = 18
A2 = 12
PR = 19

#Set ADC0831 pins
CS = 5
CLK = 6
DO = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(A1, GPIO.OUT)
GPIO.setup(A2, GPIO.OUT)
GPIO.setup(PR, GPIO.IN)

GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DO, GPIO.IN)

#This function reads the data from the ADC0831
def readADC():
    #Set initial binary string as empty
    d = ""
    
    #Set the CS pin low (Starts the conversation)
    GPIO.output(CS, False)
    
    #One clock pulse
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    #End clock pulse
    
    #Now read data synched to more clock pulses
    for n in range(0, 8): #read in 8 bits, 0-7
        #One clock pulse
        GPIO.output(CLK, False)
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)
        #End clock pulse
        
        #Listen to the DO pin for a bit
        DO_state = GPIO.input(DO)
        
        if DO_state == True:
            d = d + "1"
        else:
            d = d + "0"
        #repeat this until all the bits read
            
    #Set this CS pin high (ends conversation)
    GPIO.output(CS, True)
    
    #return the binary data to the user
    return d

#This function returns the voltage
def calc_volts(d):
    #We know voltage is on 0 to 5V scale and
    #the ADC0831 returns binary numbers with integer
    #equivalent values between 0 and 255
    d_int = int(d, 2)
    
    #We assume the voltage is exactly 5V out of the RPi
    #measure it to be sure and correct value below
    volts = 5.0 * d_int / 255
    
    #but the step size is 5V / 256 steps = 0.01953... or
    #about 0.02V V/step. Hence, we need to truncate our voltage value
    #to only display sig figs!
    volts = round(volts, 2)
    return volts


try:
    while True:
        #call the read funtion to read a binary data value
        d = readADC()
        #call the calc_volts function to calculate the resistance of the photoresistor
        volts = calc_volts(d)
        
        if volts <= 4.7:
            GPIO.output(A2, False)
            GPIO.output(A1, True)
            
        if volts > 4.7:
            GPIO.output(A1, False)
            GPIO.output(A2, True)
            
        
        time.sleep(0.5)
            
except KeyboardInterrupt:
    print("Goodbye")
    
finally:
    GPIO.cleanup()