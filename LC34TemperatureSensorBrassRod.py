#LM34 Temperature Sensor Rod

#Measure temperature with a LM34 temperature sensor

import RPi.GPIO as GPIO
import time
import math

N = 10

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
    
    volts = 3.3 * d_int / 1024
    
    volts = round(volts, 2)
    return volts

#This function converts the voltage of the sensor into a temperature value
def calc_ambient_temp(v):
    ambient_temp = (v - 0.5) / 0.01
    return ambient_temp

'''def calc_mean(temp_array):
    total = 0
    
    for i in temp_array:
        total = total + temp_array[i]
        
    average = total / N
    
    return average'''

'''def summation(temp_array, mean):
    sum = 0
    for i in temp_array:
        sum = sum + (temp_array[i] - mean) ** 2
        
    return sum'''
    

'''def calc_sd_values(sum):
    sd_values = sqrt(((1) / (N - 1)) * sum)'''

try:
    repeat = True
    count = 0
    run_time = 1800 #30 minutes
    d = [] #array to hold my binary data for each channel
    volts = []
    ambient_temp = []
    temp0 = []
    temp1 = []
    temp2 = []
    temp3 = []
    temp4 = []
    time_data = []
    
    #This setup is so I can read multiple channels at once with the same function
    channel_num = ['1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    channels = int(input("Input the number of channels (1 - 8) you want to read: "))
    
    start_time = time.time()
    
    while repeat:
        for n in range(0, channels):
            #Append the time to the time_data array
            time_data.append(time.time() - start_time)
            
            d.append(readADC_channel(channel_num[n]))

            volts.append(calc_volts(d[n]))
            
            ambient_temp.append(calc_ambient_temp(volts[n]))
            
            if n == 0:
                temp0.append(calc_ambient_temp(volts[n]))
            elif n == 1:
                temp1.append(calc_ambient_temp(volts[n]))
            elif n == 2:
                temp2.append(calc_ambient_temp(volts[n]))
            elif n == 3:
                temp3.append(calc_ambient_temp(volts[n]))
            elif n == 4:
                temp4.append(calc_ambient_temp(volts[n]))
                
            print("Voltage ", n, ": ", volts[n])
            print("Ambient Temperature", n, ": ", ambient_temp[n], "C")
    
        time.sleep(20) #records every 20 seconds
        print("\n\n")
        
        if count > N:
            repeat = False
        #Test to see if enough time has elapsed
        if time.time() - start_time > run_time:
            repeat = False
            
    #Open a data file for writing in the same directory as the working program
    file = open('TempBrassRodData.txt', 'w')
    for n in range(len(time_data)):
    
        #Write the data as comma delimited
        file.write(str(time_data[n]) + ',' + str(temp0[n]) + ',' + str(temp1[n]) + ',' + str(temp2[n]) + ',' + str(temp3[n]) + ',' + str(temp4[n]) + '\n')
    
    #Close the file
    file.close()

            
                        
except KeyboardInterrupt:
    print("Goodbye!")
    
finally:
    GPIO.cleanup()
        
        
