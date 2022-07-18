#Exam 1 - Determing useful life of a 9V battery

import RPi.GPIO as GPIO
import time

#Set ADC0831 pins
CS = 5
CLK = 6
DO = 13

#Setup
GPIO.setmode(GPIO.BCM)
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
    #measure it to be sure and correct value below and then multiply it
    #by two to realte it to the 9V battery
    volts = ((5 * d_int) / 255) * 2
    
    #but the step size is 5V / 256 steps = 0.01953... or
    #about 0.02V V/step. Hence, we need to truncate our voltage value
    #to only display sig figs!
    volts = round(volts, 2)
    
    print(volts)
    
    return volts

#Now for the main event
try:
    #Create the data arrays
    time_data = []
    voltage_data = []
    
    end = 4.8
    
    #Wait for the capacitor to charge
    time.sleep(0.5)
    
    my_test = True
    
    start_time = time.time()
    
    while my_test == True:
        #Append the time to the time_data array
        time_data.append(time.time() - start_time)
        
        
        #call the read funtion to read a binary data value
        d = readADC()
        
        #Append the binary data to the voltage_data array
        voltage_data.append(d)
        
        volts = calc_volts(d)
        
        #Test to see if enough time has elapsed
        if volts <= end:
            my_test = False
            
        time.sleep(60) #Sleep for a minute (since the program will run for a while
            
    #Open a data file for writing in the same directory as the working program
    file = open('BatteryLife.txt', 'w')
    for n in range(len(time_data)):
        my_volts = calc_volts(voltage_data[n])
        
        #Write the data as comma delimited
        file.write(str(time_data[n]) + ',' + str(my_volts) + '\n')
        
    #Close the file
    file.close()
    
    print(time.time() - start_time)
    
except KeyboardInterrupt:
    print("Initiating shutdown sequence")
    
finally:
    GPIO.cleanup()