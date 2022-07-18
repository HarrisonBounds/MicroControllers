#Harrison Bounds
#Discharging Capacitor using a 10 bit ADC chip (MCP3008)

import RPi.GPIO as GPIO
import time

#Set MCP3008 Pins
CS = 5
CLK = 6
DOUT = 13 #This pin is the data out of the chip and into the RPi
DIN = 4
cap1 = 17
cap2 = 22
cap3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(cap1, GPIO.OUT)
GPIO.setup(cap2, GPIO.OUT)
GPIO.setup(cap3, GPIO.OUT)

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

def readADC_channel_1():
    #set initial binary string
    d1 = ""
    #set the CS pin to low to start the conversation
    GPIO.output(CS, False)
    #set DIN pin high
    GPIO.output(DIN, True)
    
    #one clock pulse
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    
    #We now need to tell the chip which channel we want to read
    din_control1 = "1001" #This is the control sequence for channel 0
    
    #This loop sends the chip which channel we want to use
    for n in range(0, 4):
        result = din_control1[n]
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
            d1 = d1 + "1"
        else:
            d1 = d1 + "0"
            
    #Set the CS pin high to end the conversation
    GPIO.output(CS, True)
    
    #we need to set the DIN pin low when we are done to reset the chip
    GPIO.output(DIN, False)
    
    #return the binary data to the user
    return d1

def readADC_channel_2():
    #set initial binary string
    d2 = ""
    #set the CS pin to low to start the conversation
    GPIO.output(CS, False)
    #set DIN pin high
    GPIO.output(DIN, True)
    
    #one clock pulse
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    
    #We now need to tell the chip which channel we want to read
    din_control2 = "1010" #This is the control sequence for channel 0
    
    #This loop sends the chip which channel we want to use
    for n in range(0, 4):
        result = din_control2[n]
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
            d2 = d2 + "1"
        else:
            d2 = d2 + "0"
            
    #Set the CS pin high to end the conversation
    GPIO.output(CS, True)
    
    #we need to set the DIN pin low when we are done to reset the chip
    GPIO.output(DIN, False)
    
    #return the binary data to the user
    return d2

#This function calculates and returns the voltage
def calc_volts(d):
    #This chip returns binary values equivalent to integers between 0 and 1024! (2^10)
    d_int = int(d, 2)
    
    volts = 5 * d_int / 1024
    
    volts = round(volts, 2)
    return volts
try:
    #Create the data arrays
    time_data = []
    voltage0_data = []
    voltage1_data = []
    voltage2_data = []
    
    #Set time for experiment to run
    run_time = 0.1
    
    #Set the capacitor pins to high to charge it
    GPIO.output(cap1, True)
    GPIO.output(cap2, True)
    GPIO.output(cap3, True)
    
    #wait for the capacitors to charge
    time.sleep(0.5)
    
    my_test = True
    
    #Set capacitor pins to low
    GPIO.output(cap1, False)
    GPIO.output(cap2, False)
    GPIO.output(cap3, False)
    
    start_time = time.time()
    
    while my_test == True:
        #Append the time to the time_data array
        time_data.append(time.time() - start_time)
        
        #call the read funtion for each channel to read a binary data value
        d0 = readADC_channel_0()
        d1 = readADC_channel_1()
        d2 = readADC_channel_2()
        
        #Append the binary data to the voltage_data array
        voltage0_data.append(d0)
        voltage1_data.append(d1)
        voltage2_data.append(d2)
        
        #Test to see if enough time has elapsed
        if time.time() - start_time > run_time:
            my_test = False
            
    #Open a data file for writing in the same directory as the working program
    file = open('CapDataMCP.txt', 'w')
    for n in range(len(time_data)):
        my0_volts = calc_volts(voltage0_data[n])
        my1_volts = calc_volts(voltage1_data[n])
        my2_volts = calc_volts(voltage2_data[n])
    
        #Write the data as comma delimited
        file.write(str(time_data[n]) + ',' + str(my0_volts) + ',' + str(my1_volts) + ',' + str(my2_volts) + '\n')
    
    #Close the file
    file.close()
    
except KeyboardInterrupt:
    print("Goodbye")
    
finally:
    GPIO.cleanup()
