#tut4

'''
This tutorial deals with the basics of plotting using matplotlib

Given:
The file GW_data_file.csv contains the timeseries and the frequency data of the first Gravitational Wave detection made by LIGO, GW150914.
The data file has 3 arrays:
a) the strain data, which is filtered, so you don't have to worry about noises,
b) the frequency of the data at that particular time (Not exactly),
c) the time.

1) Your first task is to make two plots:
(a) strain vs time
(b) frequency vs time.


2) Find out the indexes of zero-crossings. Use the frequency and the time at these zero-crossings to make a frequency vs time scatter plot.

'''



import matplotlib.pyplot as plt
import numpy as np
#imports


strain, freq, time = np.loadtxt('tutorials\Tutorial_04\GW_data_file.csv',delimiter=',') #load the data into arrays


plt.plot(time,strain)
plt.xlabel('time')
plt.ylabel('strain')
plt.show()
# plotting time vs strain data, looks like an oscillating wave whos frequency and amplitude increase around time t = 0


plt.plot(time,freq)
plt.xlabel('time')
plt.ylabel('freq')
plt.show()
#plotting time vs frequency data. Is nearly constant at the start but has a sharp peak around t = 0


indexes = np.where((strain > -1)&(strain<1)) #restricting strain and time data
freq2 = freq[indexes]
time2 = time[indexes]

plt.figure(figsize=(2,2)) # figsize specifies the size of the plot
plt.scatter(time2,freq2,s=1,color='darkorange',label='Scatter') #making frequency vs time scatter plot

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()

#plt has many functions used for labeling and titling the plot
