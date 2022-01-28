#tut7
from scipy.optimize import curve_fit as cf
import matplotlib.pyplot as plt
import numpy as np


def power_law(x,a,n):
    return a*(tc-x)**n

strain, freq, time = np.loadtxt('tutorials\Tutorial_04\GW_data_file.csv',delimiter=',')

constraint_indices = np.where(freq>50)
freq2 = freq[constraint_indices]
time2 = time[constraint_indices]

tc = 0
constraint_indices = np.where(time2 < tc)
freq3 = freq2[constraint_indices]
time3 = time2[constraint_indices]

p_opt, p_cov = cf(power_law,time3,freq3)
plt.plot(time3,power_law(time3,*p_opt))
a,n = p_opt[0],p_opt[1]
c = 3 * 10**8
G = 6.67 * 10**-11
pi = np.pi
factor = (5**(3/5))/((8*pi)**(8/5)) * (c**(3))/G
mass_chirp = factor/(a**(8/5))



plt.plot(time3,freq3,'ro')
plt.xlabel('time')
plt.ylabel('freq')
plt.show()
print('chirp mass =',mass_chirp)
