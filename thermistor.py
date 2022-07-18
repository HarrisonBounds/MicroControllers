#Harrison Bounds
#Thermistor

import RPi.GPIO as GPIO
import time
import numpy as np

C1 = 0.0014
C2 = 0.00021
C3 = 4.14 * 10**(-8)

#Set ADC0831 pins
CS = 5
CLK = 6
DO = 13

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DO, GPIO.IN)

#This function calculates and returns the resistance
def calc_resistance(v):
    resistance = v / 0.00025
    return resistance
    

#This function calculates and returns the temperature given by the thermistor
def calc_temp(resistance):
    temp = (1 / (C1 + (C2 * np.log(resistance)) + (C3 * ((np.log(resistance)) ** 3)))) - 273
    return temp

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
    #print(volts)
    return volts

#Now for the main event
try:
    while True:
        #Create the data arrays
        time_data = []
        temp_data = []
    
        #Set time for experiment to run
        run_time = 20
        
        myTest = True
        
        start_time = time.time()
        
        while myTest == True:
            #Append the time to the time_data array
            time_data.append(time.time() - start_time)
            #call the read funtion to read a binary data value
            d = readADC()
            #call the calc_volts function to calculate the volts of the photoresistor
            volts = calc_volts(d)
            #call calc_resistance function
            resistance = calc_resistance(volts)
            #call the temp function and then output the temp to the user
            temp = calc_temp(resistance)
            #append the temp data to the temp array
            temp_data.append(temp)
            
            print("The temperature is: ", round(temp, 2), " degrees Celcius")
            
            #Test to see if enough time has elapsed
            if time.time() - start_time > run_time:
                myTest = False 
            print("The time elapsed is ", time.time() - start_time)
            #Sleep for 10 seconds    
            time.sleep(10)
                
        #Open a data file for writing in the same directory as the working program
        file = open('Temp vs Time', 'w')
        for n in range(len(time_data)):
            my_temp = calc_temp(temp_data[n])
    
            #Write the data as comma delimited
            file.write(str(time_data[n]) + ',' + str(my_temp) + '\n')
         
        #Close the file
        file.close()
        print("The program has stopped logging")
    
except KeyboardInterrupt:
    print("Initiating shutdown sequence")
    
finally:
    GPIO.cleanup()