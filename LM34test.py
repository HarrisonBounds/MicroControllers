import RPi.GPIO as GPIO
import time
import math

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
def readADC_channel(num):
    
    #set initial binary string
    d = ""
    #set the CS pin to low to start the conversation
    GPIO.output(CS, False)
    #set DIN pin high
    GPIO.output(DIN, True)
    
    #one clock pulse
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    
    
    #This loop sends the chip which channel we want to use
    for n in range(0, 4):
        result = num[n]
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
            d = d + "1"
        else:
            d = d + "0"
            
    #Set the CS pin high to end the conversation
    GPIO.output(CS, True)
    
    #we need to set the DIN pin low when we are done to reset the chip
    GPIO.output(DIN, False)
    
    #return the binary data to the user
    return d

#This function calculates and returns the voltage
def calc_volts(d):
    #This chip returns binary values equivalent to integers between 0 and 1024! (2^10)
    d_int = int(d, 2)
    
    volts = 5 * d_int / 1024
    
    volts = round(volts, 2)
    return volts

#This function converts the voltage of the sensor into a temperature value
def calc_ambient_temp(v):
    ambient_temp = (v - 0.5) / 0.01
    return 1.3 * ambient_temp #Adding a constant to match room temp

try:
    repeat = True
    
    #This setup is so I can read multiple channels at once with the same function
    channel_num = ['1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    channels = int(input("Input the number of channels (1 - 8) you want to read: "))
    
    while repeat:
        for n in range(0, channels):
            d = readADC_channel(channel_num[n])
            volts = calc_volts(d)
            temperature = calc_ambient_temp(volts)
            
            print("Voltage ", n, ": ", volts)
            print("Ambient Temperature", n, ": ", temperature, "C")
            time.sleep(2)
            
except KeyboardInterrupt:
    print("Goodbye!")
    
finally:
    GPIO.cleanup()