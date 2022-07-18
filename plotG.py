#plot capacitor discharge using 10 bit ADC chip
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#Define data arrays
time_data = []
position_data = []

#read in the data
lines = np.loadtxt('acceleration.txt')


for line in lines:
    time_data.append(line) #The first item in row is the time
    
for i in range(len(time_data)):
    position_data.append(i + 2.4) #cm
    
#Make a plot

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.xlim(0.6, 1)


#Make an xy scatter plot
plt.scatter(time_data, position_data, color = "red")


#Label axes and etc
ax.set_xlabel("Time(s)")
ax.set_ylabel("Position(cm)")
ax.set_title("Position vs. Time")

plt.savefig("AcceleartionDueToGravity.png")