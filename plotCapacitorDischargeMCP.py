#plot capacitor discharge using 10 bit ADC chip
import matplotlib.pyplot as plt
import numpy as np

#Define data arrays
time_data = []
voltage0_data = []
voltage1_data = []
voltage2_data = []

#read in the data
lines = np.loadtxt('CapDataMCP.txt', delimiter = ',')


for line in lines:
    time_data.append(line[0]) #The first item in row is the time
    voltage0_data.append(line[1]) #The second item in the row is the voltage from channel 0
    voltage1_data.append(line[2]) #The second item in the row is the voltage from channel 1
    voltage2_data.append(line[3]) #The second item in the row is the voltage from channel 2
    
#exponential decay function
def my_func(x, a, b):
    return a * np.exp(-b * x)

#Have to do the following to use time data in the exponential function
fit_time_data1 = np.array(time_data)

#Make a plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#Make an xy scatter plot
plt.scatter(time_data, voltage0_data, color = "red", label = "10K Resistor")
plt.scatter(time_data, voltage1_data, color = "blue", label = "20K Resistor")
plt.scatter(time_data, voltage2_data, color = "green", label = "30K Resistor")

#Add exponential curve with guesses for the constants a and b
plt.plot(fit_time_data1, my_func(fit_time_data1, 3.3, 95), color = "black", label = "my fit 10k")
plt.plot(fit_time_data1, my_func(fit_time_data1, 3.3, 45), color = "black", label = "my fit 20K")
plt.plot(fit_time_data1, my_func(fit_time_data1, 3.3, 30), color = "black", label = "my fit 30K")

#Label axes and etc
ax.set_xlabel("Time(s)")
ax.set_ylabel("Voltage(V)")
ax.set_title("Capacitor Discharge")

plt.legend(loc = "upper right") #Legend location can be changed

ax.text(0.4, 1.5, "Annotate the plot if needed")
plt.savefig("CapDischargesMCP.png")