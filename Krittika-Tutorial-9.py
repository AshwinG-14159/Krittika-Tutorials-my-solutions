#tut9
'''

This tutorial has 2 parts, second part is yet to be completed. First part- higher order matplotlib functionaities. Especially the object oriented approach to matplotlib plots.

Given:
The data has been provided to you in the 'NGC5272.csv', which contains data for the globular cluster M3. The columns indicate different wavelength bands.


Task:
1) To plot the HR diagram (or rather the color-magnitude diagram) of the given cluster, in different color bands. (See explanation below)
2) Once you have made 4 such plots, put them in a 2 by 2 subplot grid with both the x and y axes shared and each subplot and the axes labeled.

Your job is to plot HR diagrams for pairwise filters, sequentially, i.e., F275W vs F275W-F336W, F336W vs F336W-F438W, F438W vs F438W-F606W and 
F606W vs F606W-F814W. The last column gives the probability of individual stars (you have encountered this before; -1.0 indicates data for the given star 
is not available). Use this probability to filter out low probability stars, and ensure the orientation of the axes based on the properties of the HR diagram mentioned above.


Based on your plots try to reason which color is the best to study the cluster in, and why.


'''
import matplotlib.pyplot as plt
import numpy as np
#imports




data = np.loadtxt('tutorials//Tutorial_09//NGC5272.csv',usecols = (1,2,3,4,5,6))
min_p = 80
data = data[np.where(data[:,5] > min_p)]
F_275 = data[:,0]
F_336 = data[:,1]
F_438 = data[:,2]
F_606 = data[:,3]
F_814 = data[:,4]
prob = data[:,5]
#load the data into arrays


fig,axes = plt.subplots(2,2,sharex = 'all', sharey = 'all')
fig.suptitle('HR Diagram')
#create subplots sharing both axes

axes[1,0].set_xlim(-2.0, 5)
axes[1,0].set_ylim(30, 11)
#scaling the axes to required range

axes[0,0].scatter(F_275-F_336,F_275, s=0.03)
axes[0,1].scatter(F_336-F_438,F_336, s=0.03)
axes[1,0].scatter(F_438-F_606,F_438, s=0.03)
axes[1,1].scatter(F_606-F_814,F_606, s=0.03)
#plotting the scatter plots


for axis in axes.flat:
    axis.set_xlabel('Color')
    axis.set_ylabel('Intensity')
#setting labels

'''
data on part 2 of tut 9 will be uploaded soon
'''



