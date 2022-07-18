#plot capacitor discharge using 10 bit ADC chip
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#Define data arrays
time_data = []
voltage_data = []

#read in the data
lines = np.loadtxt('BatteryLife.txt', delimiter = ',')


for line in lines:
    time_data.append(line[0] / 3600) #The first item in row is the time
    voltage_data.append(line[1]) #The second item in the row is the voltage from channel 0


#Make a plot

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.ylim(4.5, 9)


#Make an xy scatter plot
plt.scatter(time_data, voltage_data, color = "red")


#Label axes and etc
ax.set_xlabel("Time(h)")
ax.set_ylabel("Voltage(V)")
ax.set_title("9V Battery Voltage continous discharge through 200 Ohms")

plt.savefig("BatteryDischarge.png")