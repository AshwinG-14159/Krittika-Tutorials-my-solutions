#tut 2
'''
This tutorial is an introduction to numpy. 

Given: in Beehive_data.csv, the columns are respectively the apparent magnitude of the stars as seen from Earth,
the logarithm of the Luminosity(in units of Luminosity of the Sun) of the stars (i.e.  log(𝐿/𝐿⊙) , where  𝐿⊙  is the luminosity of the sun), 
and the probability that the star belongs to the Beehive Cluster.



Task:
Use the data from Beehive_data.csv to find the distance to the Beehive Cluster (you are given that the absolute magnitude of the Sun is +4.83).


'''




import numpy as np


beehive_data = np.loadtxt('tutorials\Tutorial_02\Beehive_data.csv', delimiter=',') #loading behive data into numpy array


log_d = 0.2*(beehive_data[:,0] + 2.5*beehive_data[:,1] + 0.17) #using magnitude calculations, this gives an array of log of distances to the stars 

weighted_d_list = beehive_data[:,2]*(10**log_d) 
# calculate a weighted list based on the probabilities of each star being in the cluster. 
#Stars with low probabilities will hence contribute less to the calculations


dist_sum = 0
i_sum = 0

for i in range(len(weighted_d_list)):
    dist_sum += weighted_d_list[i]
    i_sum += beehive_data[i,2]
                        # find weighted mean and print
answer = dist_sum/i_sum
print(answer)



