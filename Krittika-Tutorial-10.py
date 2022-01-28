#tut10

import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from astropy.io import fits
from astropy import units as u 

SDSS_filter = fits.open('tutorials//Tutorial_10//filter_curves.fits')

U = SDSS_filter[1].data
G = SDSS_filter[2].data
R = SDSS_filter[3].data
I = SDSS_filter[4].data
Z = SDSS_filter[5].data

intensity_G = 1.3887e-09 * (u.W / u.m**2)
intensity_R = 2.5553e-09 * (u.W / u.m**2)

ratio_arcturus = intensity_G/intensity_R

wlG = G['wavelength']*u.AA
qG = G['respt']
wlR = R['wavelength']*u.AA
qR = R['respt']

c = const.c
kB = const.k_B
h = const.h


def B(wl,T):
    exponential = 1/(np.exp(h*c/(wl*kB*T))-1)
    prefactor = 2*np.pi*h*c*c/wl**5
    return prefactor*exponential


def G_R_ratio(T):
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

Temps = np.arange(500,10000,100)*u.K
GR = []
for t in Temps:
    GR.append(G_R_ratio(t))


difference = np.abs(GR - ratio_arcturus)
T_arcturus = Temps[np.where(difference == np.amin(difference))][0]
print(T_arcturus)

