import RPi.GPIO as GPIO
import time
import math

#Set MCP3008 Pins
CS = 5
CLK = 6
DOUT = 13 #This pin is the data out of the chip and into the RPi
DIN = 4
relay_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DOUT, GPIO.IN)
GPIO.setup(DIN, GPIO.OUT)
GPIO.setup(relay_pin, GPIO.OUT)

#set up the LED as a PWM object
freq = 100 #Hertz
my_pwm = GPIO.PWM(LED, freq)

#start the object
duty_cycle = 0 #percentage, 0% = OFF, 100% = fully ON
my_pwm.start(duty_cycle)

pause_time = 1 #seconds

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
    return ambient_temp #Adding a constant to match room temp

def bang_bang():
    
    

try:
    repeat = True
    switch = 0
    hold_time = 200
    hold_time2 = 400 + hold_time + 100 # 100 accounts for the drop in temp
    cool_time = 400 + hold_time2
    t_set_point = 50.5
    t_set_point2 = 30.5
    
    d = [] #array to hold my binary data for each channel
    volts = []
    temperature = []
    time_data = []
    
    choice = input("Bang-Bang control(b) or Proportional Control(p)?: ")
    
    #This setup is so I can read multiple channels at once with the same function
    channel_num = ['1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
    channels = int(input("Input the number of channels (1 - 8) you want to read: "))
    
    start_time = time.time()
    
    while repeat:
        for n in range(0, channels):
            time_data.append(time.time() - start_time)
            
            d.append(readADC_channel(channel_num[n]))
            volts.append(calc_volts(d[n]))
            temperature.append(calc_ambient_temp(volts[n]))
            
            d_read = readADC_channel(channel_num[n])
            volts_read = calc_volts(d_read)
            temperature_read = calc_ambient_temp(volts_read)
            
            if choice == "b":
            
                if switch == 0:
                    if temperature_read < 50: #Degrees in celcius
                        GPIO.output(relay_pin, True)
                    if temperature_read > 51:
                        GPIO.output(relay_pin, False)
                        
                    if time.time() - start_time > hold_time:
                        switch = 1
                    
                if switch == 1:
                    if temperature_read < 30: #Degrees in celcius
                        GPIO.output(relay_pin, True)
                    if temperature_read > 31:
                        GPIO.output(relay_pin, False)
                        
                    if time.time() - start_time > hold_time2:
                        switch = 2
                            
                if switch == 2:
                    GPIO.output(relay_pin, False)
                    if time.time() - start_time > cool_time:
                            repeat = False
                            
            if choice == "p":
                t_error = t_set_point - temperature_read
                t_error2 = t_set_point2 - temperature_read
                
                while t_error > 0 and t_error < 10:
                    my_pwm.ChangeDutyCycle(40) #40% 
                    
                while t_error > 10:
                    my_pwm.ChangeDutyCycle(90) #90% 
                    
                while t_error < 0:
                    my_pwm.ChangeDutyCycle(0)
                
                
            
            print("Voltage: ", volts_read)
            print("Temperature: ", temperature_read, "C")
            time.sleep(0.25)
    if choice == "b":
        name = "bang.txt"
    if choice == "p":
        name = "proportional.txt"
        
    #Open a data file for writing in the same directory as the working program
    file = open(name, 'w')
    for n in range(len(time_data)):
    
        #Write the data as comma delimited
        file.write(str(time_data[n]) + ',' + str(temperature[n]) + '\n')
    
    #Close the file
    file.close()

            
except KeyboardInterrupt:
    print("Goodbye!")
    
finally:
    GPIO.cleanup()
