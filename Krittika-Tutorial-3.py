#tut3

import numpy as np
import math as mt

def extract_data(ser_no):
    location = np.where(gal_data[:,0] == ser_no)
    RA = float(gal_data[location,1])
    dec = float(gal_data[location,2])
    redshift = float(gal_data[location,3])
    return(ser_no,RA,dec,redshift)


def gal_dist(ser_no):
    data = extract_data(ser_no)
    speed = data[3]*c
    dist = speed/H0
    return(dist)
    

def include_distance():
    inc_dist = np.empty((len(gal_data),5))
    inc_dist[:,0:4] = gal_data[:,0:4]
    for i in range(len(gal_data[:,0])):
        inc_dist[i,4] = gal_dist(gal_data[i,0])
    return inc_dist

def gal_in_range(d1,d2):
    location = np.where((gal_data[:,4] > d1)&(gal_data[:,4] < d2))
    return len(gal_data[location])

def angular_sep(r1,r2,d1,d2):
    cos_angle = mt.sin(d1)*mt.sin(d2) + mt.cos(d1)*mt.cos(d2)*mt.cos(r1-r2)
    return mt.acos(cos_angle)

def dist_between_gal(s1,s2):
    d1 = extract_data(s1)
    d2 = extract_data(s2)
    angle = angular_sep(d1[1]*pi/180,d2[1]*pi/180,d1[2]*pi/180,d2[2]*pi/180)
    dist1,dist2 = gal_dist(s1),gal_dist(s2)
    dist = mt.sqrt((dist1**2) + (dist2**2) - 2*dist1*dist2*mt.cos(angle))
    return dist


c = 3*10**5
H0 = 70
pi = mt.pi

gal_data = np.loadtxt('tutorials\Tutorial_03\galaxies.csv', delimiter=',')


index = int(input("enter ser num: "))
print(gal_dist(index))

gal_data = np.array(include_distance())

d1 = float(input("enter d1: "))
d2 = float(input("enter d2: "))

print(gal_in_range(d1, d2))

s1 = int(input("ser1: "))
s2 = int(input("ser2: "))

print(dist_between_gal(s1,s2))
