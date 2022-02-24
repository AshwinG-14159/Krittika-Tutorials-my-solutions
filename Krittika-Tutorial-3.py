#tut3

'''
This tutorial was mainly about the use of functions in python


Given: 
You are given a 'galaxies.csv' file which contains data for galaxies observed by the Sloan Digital Sky Survey(SDSS) - Mapping Nearby Galaxies At 
Apache Point Observatory(MaNGA). The file contains basic properties of each galaxy observed, namely the following:

1) serialno - A Serial Number we have assigned to each galaxy
2) objra (in degrees) - The Right Ascension of the galaxy
3) objdec (in degrees) - The Declination of the galaxy
4) redshift - The observed redshift in the spectra of the galaxy



Task:

1) Compute the distance to a galaxy, in suitable units, given the galaxy's serial number.

2) Compute the number of galaxies observed by SDSS-MaNGA, in some given distance interval.

3) Compute the physical separation between two galaxies, given their serial numbers. Note: The two galaxies might be at different radial distances.


'''



import numpy as np
import math as mt
#imports

def extract_data(ser_no):     #returns all the data in proper format and datatype from the complete gal_data array. Takes serial number of galaxy to be searched as input
    location = np.where(gal_data[:,0] == ser_no)
    RA = float(gal_data[location,1])
    dec = float(gal_data[location,2])
    redshift = float(gal_data[location,3])
    return(ser_no,RA,dec,redshift)


def gal_dist(ser_no):          # provides distance to a galaxy from its serial number. Extraxt data on the galaxy and then use Hubble's law on the redshift for the distance. 
    data = extract_data(ser_no)
    speed = data[3]*c
    dist = speed/H0
    return(dist)
    

def include_distance():       # include the distance to a galaxy as a column in the numpy array. Need the distance a lot for following calculations
    inc_dist = np.empty((len(gal_data),5))
    inc_dist[:,0:4] = gal_data[:,0:4]
    for i in range(len(gal_data[:,0])):
        inc_dist[i,4] = gal_dist(gal_data[i,0])
    return inc_dist

def gal_in_range(d1,d2):     # returns number of galaxies in range d1-d2 from the array
    location = np.where((gal_data[:,4] > d1)&(gal_data[:,4] < d2))
    return len(gal_data[location])

def angular_sep(r1,r2,d1,d2):  #find angular separation in galaxies, given their right ascensions and decinations. Use spherical trigonometry
    cos_angle = mt.sin(d1)*mt.sin(d2) + mt.cos(d1)*mt.cos(d2)*mt.cos(r1-r2)
    return mt.acos(cos_angle)

def dist_between_gal(s1,s2):  # Returns distance between 2 galaxies by using cosine rule. Angular separation calculated using angular_sep() function and distance to individual galaxies given
    d1 = extract_data(s1)
    d2 = extract_data(s2)
    angle = angular_sep(d1[1]*pi/180,d2[1]*pi/180,d1[2]*pi/180,d2[2]*pi/180)
    dist1,dist2 = gal_dist(s1),gal_dist(s2)
    dist = mt.sqrt((dist1**2) + (dist2**2) - 2*dist1*dist2*mt.cos(angle))
    return dist


c = 3*10**5
H0 = 70
pi = mt.pi
#some physical constants

gal_data = np.loadtxt('tutorials\Tutorial_03\galaxies.csv', delimiter=',') #loading data into numpy array

# part 1 - print distance to galaxy from serial number

index = int(input("enter ser num: "))
print(gal_dist(index))

# part 2 - find number of galaxies in a certain range of distance
gal_data = np.array(include_distance())

d1 = float(input("enter d1: "))
d2 = float(input("enter d2: "))

print(gal_in_range(d1, d2))

# part 3 - find distance betwen 2 given galaxies

s1 = int(input("ser1: "))
s2 = int(input("ser2: "))

print(dist_between_gal(s1,s2))
