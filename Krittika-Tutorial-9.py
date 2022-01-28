#tut9

import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('tutorials//Tutorial_09//NGC5272.csv',usecols = (1,2,3,4,5,6))
min_p = 80
data = data[np.where(data[:,5] > min_p)]
F_275 = data[:,0]
F_336 = data[:,1]
F_438 = data[:,2]
F_606 = data[:,3]
F_814 = data[:,4]
prob = data[:,5]

fig,axes = plt.subplots(2,2,sharex = 'all', sharey = 'all')
fig.suptitle('HR Diagram')

axes[1,0].set_xlim(-2.0, 5)
axes[1,0].set_ylim(30, 11)


axes[0,0].scatter(F_275-F_336,F_275, s=0.03)
axes[0,1].scatter(F_336-F_438,F_336, s=0.03)
axes[1,0].scatter(F_438-F_606,F_438, s=0.03)
axes[1,1].scatter(F_606-F_814,F_606, s=0.03)

for axis in axes.flat:
    axis.set_xlabel('Color')
    axis.set_ylabel('Intensity')

