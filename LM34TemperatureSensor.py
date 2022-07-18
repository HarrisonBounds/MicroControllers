#Measure temperature with a LM34 temperature sensor

import RPi.GPIO as GPIO
import time

#Set MCP3008 Pins
CS = 5
CLK = 6
DOUT = 13 #This pin is the data out of the chip and into the RPi
DIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(DIN, GPIO.OUT)

#This function reads the MCP3008 data
#Note that this function is specific to channel 0... Modify this to read other channels
def readADC_channel_0():
    #set initial binary string
    d0 = ""
    #set the CS pin to low to start the conversation
    GPIO.output(CS, False)
    #set DIN pin high
    GPIO.output(DIN, True)
    
    #one clock pulse
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    
    #We now need to tell the chip which channel we want to read
    din_control0 = "1000" #This is the control sequence for channel 0
    
    #This loop sends the chip which channel we want to use
    for n in range(0, 4):
        result = din_control0[n]
        if result == "1":
            GPIO.output(DIN, True)
        elif result == "0":
            GPIO.output(DIN, False)  
        #one clock pulse
        GPIO.output(CLK, False)
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)
        
    #one clock pulse
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    
    #Now we need to actually read the data
    for n in range(0, 10):
        #one clock pulse
        GPIO.output(CLK, False)
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)
        
        #listen to the DOUT pin for a bit
        DO_state = GPIO.input(DOUT)
        if DO_state == True:
            d0 = d0 + "1"
        else:
            d0 = d0 + "0"
            
    #Set the CS pin high to end the conversation
    GPIO.output(CS, True)
    
    #we need to set the DIN pin low when we are done to reset the chip
    GPIO.output(DIN, False)
    
    #return the binary data to the user
    return d0

#This function calculates and returns the voltage
def calc_volts(d):
    #This chip returns binary values equivalent to integers between 0 and 1024! (2^10)
    d_int = int(d, 2)
    
    volts = 5 * d_int / 1024
    
    volts = round(volts, 2)
    return volts

#This function converts the voltage of the sensor into a temperature value
def calc_temp(v):
    temp = v * 100
    return temp

try:
    while True:
        d = readADC_channel_0()
        volts = calc_volts(d)
        temp = calc_temp(volts)
        
        print("Voltage: ", volts)
        print("Temperature: ", temp, "F")
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("Goodbye!")
    
finally:
    GPIO.cleanup()
        
        

    
