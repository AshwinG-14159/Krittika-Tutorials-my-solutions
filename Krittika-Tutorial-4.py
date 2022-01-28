#tut4
import matplotlib.pyplot as plt
import numpy as np



strain, freq, time = np.loadtxt('tutorials\Tutorial_04\GW_data_file.csv',delimiter=',')

plt.plot(time,strain)
plt.xlabel('time')
plt.ylabel('strain')
plt.show()

plt.plot(time,freq)
plt.xlabel('time')
plt.ylabel('freq')
plt.show()

indexes = np.where((strain > -1)&(strain<1))
freq2 = freq[indexes]
time2 = time[indexes]

plt.figure(figsize=(2,2)) # figsize specifies the size of the plot
plt.scatter(time2,freq2,s=1,color='darkorange',label='Scatter')
                                                                   #  at once same as normal plots
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()

