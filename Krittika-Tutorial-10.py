#tut10

'''
This tutorial mainly deals with the astropy module. It explains the working of units in astronomy and how the astropy module can be used to keep track of units and constants.
It tackles astronomical filters as an astrophysics topic.

Given: 

for star Arcturus, the intensities in 2 wavelength bands are given - 
intensity_G = 1.3887e-09 * (u.W / u.m**2)
intensity_R = 2.5553e-09 * (u.W / u.m**2)

Properties of the filters used to measure these values are given in file filter_curves.fits.

Task:
Estimate the temperature of Arcturus to within  ±50𝐾 . You may assume that Arcturus behaves like a perfect blackbody.

'''


import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from astropy.io import fits
from astropy import units as u 
#imports

SDSS_filter = fits.open('tutorials//Tutorial_10//filter_curves.fits')

G = SDSS_filter[2].data
R = SDSS_filter[3].data

#Get filter data i.e properties of the filters that produced the filter data

intensity_G = 1.3887e-09 * (u.W / u.m**2)
intensity_R = 2.5553e-09 * (u.W / u.m**2)

ratio_arcturus = intensity_G/intensity_R # this ratio should be achieved using the black body curve at and around T_Arcturus

wlG = G['wavelength']*u.AA
qG = G['respt']
wlR = R['wavelength']*u.AA
qR = R['respt']
#extracting flter data

c = const.c
kB = const.k_B
h = const.h
#constants

def B(wl,T):      #planck's law function at given wavelenth and temperature
    exponential = 1/(np.exp(h*c/(wl*kB*T))-1)
    prefactor = 2*np.pi*h*c*c/wl**5
    return prefactor*exponential



def G_R_ratio(T):      #numeric integration for a blackbody at given Temperature to get ratio in G and R filter(for the given filters with the given properties)
    integral_G = 0*u.W/u.m**2
    integral_R = 0*u.W/u.m**2
    i = 1
    while i < len(wlR):
        integral_R += B((wlR[i-1]+wlR[i])/2 , T)*(qR[i-1]+qR[i])/2*(wlR[i]-wlR[i-1])
        i = i + 1
    j = 1
    while j < len(wlG):
        integral_G += B((wlG[j-1]+wlG[j])/2 , T)*(qG[j-1]+qG[j])/2*(wlG[j]-wlG[j-1])
        j = j + 1
    return (integral_G/integral_R)

Temps = np.arange(500,10000,100)*u.K # a range of emperature to experiment on
GR = []
for t in Temps:
    GR.append(G_R_ratio(t))


difference = np.abs(GR - ratio_arcturus)
T_arcturus = Temps[np.where(difference == np.amin(difference))][0]  #selecting temperature where G_R_ratio is closest to the experimentally measured one
print(T_arcturus)

