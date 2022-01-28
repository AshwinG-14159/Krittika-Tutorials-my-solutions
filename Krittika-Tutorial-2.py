#tut 2
import numpy as np


beehive_data = np.loadtxt('tutorials\Tutorial_02\Beehive_data.csv', delimiter=',')


log_d = 0.2*(beehive_data[:,0] + 2.5*beehive_data[:,1] + 0.17)
weighted_d_list = beehive_data[:,2]*(10**log_d)


dist_sum = 0
i_sum = 0

for i in range(len(weighted_d_list)):
    dist_sum += weighted_d_list[i]
    i_sum += beehive_data[i,2]
    
answer = dist_sum/i_sum
print(answer)



