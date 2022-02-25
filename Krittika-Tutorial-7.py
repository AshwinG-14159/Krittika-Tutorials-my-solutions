#tut7

'''

This tutorial introduces the basics of the scipy module.

For this, you'll need your results from Tutorial 4 which was on plotting. If you got your results correct, you should see a monotonically increasing function. 
According to General Relativity, we know that the frequency-time relationship is a power law. This equation is present at the following link:

https://en.wikipedia.org/wiki/Chirp_mass

 
Where  𝑓𝐺𝑊  is the frequency of Gravitational Waves,    is the chirp mass of the Binary system and  𝑡𝑐  is the time of
coalescence, the time with the t=0 mark in your data. Note that this equation is applicable only for  𝑡<𝑡𝑐 , as after this is the ringdown where
the process is highly non-linear and it is not possible to predict the equation followed by the frequency.

You can find more about the event in this paper.

Your task:

Your task is to take points with frequency higher than 50 Hz until  𝑡𝑐  and fit a curve to get the chirp mass of the system.



'''




from scipy.optimize import curve_fit as cf
import matplotlib.pyplot as plt
import numpy as np
#imports


def power_law(x,a,n):  #sample function for fitting power law
    return a*(tc-x)**n

strain, freq, time = np.loadtxt('tutorials\Tutorial_04\GW_data_file.csv',delimiter=',') #data input

constraint_indices = np.where(freq>50)
freq2 = freq[constraint_indices]
time2 = time[constraint_indices]

tc = 0
constraint_indices = np.where(time2 < tc)
freq3 = freq2[constraint_indices]
time3 = time2[constraint_indices]

#select data with constraints on frequency and time to fit the power law curve to this data

p_opt, p_cov = cf(power_law,time3,freq3 #curve fit the function constraints
plt.plot(time3,power_law(time3,*p_opt))  #plotting the curve
a,n = p_opt[0],p_opt[1]
c = 3 * 10**8
G = 6.67 * 10**-11
pi = np.pi
factor = (5**(3/5))/((8*pi)**(8/5)) * (c**(3))/G
mass_chirp = factor/(a**(8/5))
# calculating the chirp mass


plt.plot(time3,freq3,'ro') #plot the data points
plt.xlabel('time')
plt.ylabel('freq')
plt.show()
print('chirp mass =',mass_chirp)
