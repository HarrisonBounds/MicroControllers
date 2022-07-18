#Harrison Bounds
#Plotting capacitor discharge data

import matplotlib.pyplot as plt
import numpy as np

#Define data arrays
time1_data = []
voltage1_data = []

time2_data = []
voltage2_data = []

time3_data = []
voltage3_data = []

#read in the data
line1 = np.loadtxt('CapData_1Kohm.txt', delimiter = ',')
line2 = np.loadtxt('CapData_20Kohm.txt', delimiter = ',')
line3 = np.loadtxt('CapData_30Kohm.txt', delimiter = ',')

for line in line1:
    time1_data.append(line[0]) #The first item in row is the time
    voltage1_data.append(line[1]) #The second item in the row is the voltage
    
for line in line2:
    time2_data.append(line[0]) #The first item in row is the time
    voltage2_data.append(line[1]) #The second item in the row is the voltage
    
for line in line3:
    time3_data.append(line[0]) #The first item in row is the time
    voltage3_data.append(line[1]) #The second item in the row is the voltage
    
#exponential decay function
def my_func(x, a, b):
    return a * np.exp(-b * x)

#Have to do the following to use time data in the exponential function
fit_time_data1 = np.array(time1_data)
fit_time_data2 = np.array(time2_data)
fit_time_data3 = np.array(time3_data)

#Make a plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#Make an xy scatter plot
plt.scatter(time1_data, voltage1_data, color = "red", label = "1K Resistor")
plt.scatter(time2_data, voltage2_data, color = "blue", label = "20K Resistor")
plt.scatter(time3_data, voltage3_data, color = "green", label = "30K Resistor")

#Add exponential curve with guesses for the constants a and b
plt.plot(fit_time_data1, my_func(fit_time_data1, 3.3, 95), color = "black", label = "my fit")
plt.plot(fit_time_data2, my_func(fit_time_data2, 3.3, 95), color = "black", label = "my fit")
plt.plot(fit_time_data3, my_func(fit_time_data3, 3.3, 95), color = "black", label = "my fit")

#Label axes and etc
ax.set_xlabel("Time(s)")
ax.set_ylabel("Voltage(V)")
ax.set_title("Capacitor Discharge")

plt.legend(loc = "upper right") #Legend location can be changed

ax.text(0.4, 1.5, "Annotate the plot if needed")
plt.savefig("CapDischargeForDifferentResistances.png")