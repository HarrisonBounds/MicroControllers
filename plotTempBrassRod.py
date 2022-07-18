#Plot data of Temperature Brass Rod
import matplotlib.pyplot as plt
import numpy as np



#read in the data#plot capacitor discharge using 10 bit ADC chip
import matplotlib.pyplot as plt
import numpy as np

#Define data arrays
time_data = []
temp0_data = []
temp1_data = []
temp2_data = []
temp3_data = []
temp4_data = []

#read in the data
lines = np.loadtxt('TempBrassRodData.txt', delimiter = ',')


for line in lines:
    time_data.append(line[0]) #The first item in row is the time
    temp0_data.append(line[1]) #The second item in the row is the voltage from channel 0
    temp1_data.append(line[2]) 
    temp2_data.append(line[3])
    temp3_data.append(line[4])
    temp4_data.append(line[5])


#Make a plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.xlim(0, 320)
plt.ylim(0, 25)

#Make an xy scatter plot
plt.scatter(time_data, temp0_data, color = "green", label = "Top sensor")
plt.scatter(time_data, temp1_data, color = "green", label = "Second Sensor")
plt.scatter(time_data, temp2_data, color = "green", label = "Middle Sensor")
plt.scatter(time_data, temp3_data, color = "yellow", label = "Fourth Sensor")
plt.scatter(time_data, temp4_data, color = "orange", label = "Bottom Sensor")


#Label axes and etc
ax.set_xlabel("Time(sec)")
ax.set_ylabel("Temp(C)")
ax.set_title("Temperature Change Across 5 sensors on a Brass Rod")

plt.legend(loc = "upper right") #Legend location can be changed

plt.savefig("TempBrassRodGraph.png")

