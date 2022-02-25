#tut6 q1

'''
This tutorial covers some basic concepts of web scraping. i.e accessing a webpage using python and extracting its data. 

Given: wikipedia page of constellations("https://en.wikipedia.org/wiki/Lists_of_stars_by_constellation") and of 
moons and planets("https://en.wikipedia.org/wiki/List_of_natural_satellites").

Task:
1) Parse this webpage for the RA and Dec of stars of each constellation, convert these coordinates to Cartesian coordinates 
and store them by constellation and plot them using matplotlib.

2)Try to recreate the 'Moons_and_planets.csv' file(used in the first tutorial) from this webpage. You can take inspiration from 
how tables are scraped in the get_map() function for Task 1. Do remember to remove commas and uncertainties in the radius measurement.
'''

import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
#imports


def get_coords(ra_s, dec_s):  # returns right ascencsion and declination given ra and dec in string format.
    h_ind = ra_s.find('h')
    m_ind = ra_s.find('m')
    s_ind = ra_s.find('s')    
    h = float(ra_s[:h_ind])
    m = float(ra_s[(h_ind+1):m_ind])
    s = float(ra_s[(m_ind+1):s_ind])
    ra = h + m/60 + s/3600
    if dec_s[0] == '+':
        sign = 1                #check for positive and negative sign
    else:
        sign = -1
    d_ind = dec_s.find('°')
    m_ind = dec_s.find('′')
    s_ind = dec_s.find('″')
    d = float(dec_s[1:d_ind])
    m = float(dec_s[(d_ind+1):m_ind])
    s = float(dec_s[(m_ind+1):s_ind])
    dec = sign*(d + m/60 + s/3600)
    return ra, dec


def get_map(constellation):     #returns stars data for a constellations given a constellation. Returns arrays for names, positions, magnitudes
    url = f'https://en.wikipedia.org/wiki/List_of_stars_in_{constellation}' #page gets downloaded according to constellation
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'lxml')  #Here, the lxml parser is used instead of HTML parser

    tab = soup.find_all('table', attrs={'class':'wikitable sortable'})[0]   #To extract information from a wikipedia table
                               
    data = [[]]
    for i in tab.find_all('tr'):   #searching in each row of the table ( 'tr' tag stands for row)
        row = []                    #declaring empty row
        for j in i.find_all('td'):  #'td' tag stands for a cell
            row.append(j.get_text())   #add the text contents of each row to the list
        data.append(row)

    heads = []
    for i in tab.find_all('tr')[:1]:
        for j in i.find_all('th'):             #'th' tag stands for header cell
            heads.append(j.get_text().strip('\n'))

    name_ind = heads.index('Name')
    ra_ind = heads.index('RA')
    dec_ind = heads.index('Dec')
                                  
    mag_ind = heads.index('abs.mag.')
    
    #  indices of all the main data points are stored
        
    name = []
    ra = []
    dec = []
    mag = []
    for i in data[2:-2]:
        name_string = i[name_ind]
        try:                                             #The code first tries to run the code inside try
            ra_string = i[ra_ind].replace('\xa0', '')
            dec_string = i[dec_ind].replace('\xa0', '')   #These are code used to format the data
            mag_string = i[mag_ind]                       
            if mag_string[0]=='−':
                mag_string = '-'+mag_string[1:]
        except:                                       #If any error gets thrown up, it will execute the code inside except
            continue
        try:
            ra_i, dec_i = get_coords(ra_string, dec_string)     #convert ra dec from string to float
        except:
            continue
        try:
            mag.append(float(mag_string))
            name.append(name_string)
            ra.append(ra_i)
            dec.append(dec_i)
        except:
            continue

    name = np.array(name)
    ra = np.array(ra)
    dec = np.array(dec)
    mag = np.array(mag)
    return name, ra, dec, mag

    
    
def get_const_data(): #get data for all constellations into a big list
    page = requests.get("https://en.wikipedia.org/wiki/Lists_of_stars_by_constellation")
    space_soup = BeautifulSoup(page.content, 'html.parser')
#print(space_soup.prettify())

    items = space_soup.find_all('li')[5:93]
    
    big_list = []
    
    for i in items:   #iterate over all given constellation names and find their data. Add it to the big list
        print(i.get_text())
        name_list,ra_list,dec_list,mag_list = get_map(i.get_text())
        big_list.append([i.get_text(),name_list,ra_list,dec_list,mag_list])
    
    return big_list


def process_data(big_list):
    big_list2 = []
    for i in big_list:
        star_names = []
        star_ra = []
        star_dec = []
        star_mag = []
        for j in range(len(i[1])):
            if len(i[1][j]) > 0:
                value = i[1][j][:-4]
                star_names.append(str(value))
                star_ra.append(i[2][j])
                star_dec.append(i[3][j])
                star_mag.append(i[4][j])
        star_names,star_ra,star_dec,star_mag = np.array(star_names),np.array(star_ra),np.array(star_dec),np.array(star_mag)
        term = [i[0],star_names,star_ra,star_dec,star_mag]
        big_list2.append(term)
    return(big_list2)  # remove null values and get a processed big list. call it big_list2


def project(ra, dec): # Stereographic Projection. Used spherical trigonometry
    theta = np.deg2rad(90-dec + dec.mean())
    phi = np.deg2rad((ra-ra.mean())*15)
    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(theta)
    X = x/(1-z)
    Y = y/(1-z)
    return X,Y
    
    

def plot_const(const):  #plot contellations data with suitable scaling, resizing etc
    const_data = []
    for i in big_list2:
        if i[0] == const:
            const_data = i
            break
    name,ra,dec,mag = const_data[1],const_data[2],const_data[3],const_data[4]
    mag += 3
    mag = (10**(-mag))
    print(mag)
    plt.scatter(ra,dec,s = mag)
    plt.show()
    
big_list = get_const_data()
big_list2 = process_data(big_list)
for i in big_list2:
    x,y = project(i[2],i[3])
    i[2], i[3] = x,y 

#main code


const = input("constellation: ")
plot_const(const)


'''    
End of Q1

Q2 ahead

'''


#tut6 q2


page = requests.get("https://en.wikipedia.org/wiki/List_of_natural_satellites")
soup = BeautifulSoup(page.content, 'html.parser')

planets_t = soup.find_all('table',attrs = {'class':'wikitable sortable'})[0]

planets_d = []
for i in planets_t.find_all('tr'):
    row = []
    for j in i.find_all('td'):
        value = j.get_text()
        value = value.replace(',','')
        row.append(value)
    planets_d.append(row)    #get planet data into list planets_d

heads = []
for i in planets_t.find_all('tr')[:1]:
    for j in i.find_all('th'):             #'th' tag stands for header cell
        heads.append(j.get_text().strip('\n'))        #get header data into list heads

index_name_moon = heads.index('Name')
index_name_planet = heads.index('Parent')
index_radius = heads.index('Mean radius (km)')

#get important quantities

csv_data = ["Name of moon","Name of planet","Mean radius(km)"]
for i in planets_d:
    if len(i) !=0:
        name_moon,name_planet,radius = i[index_name_moon],i[index_name_planet],i[index_radius]
        radius = radius.split('±')[0]
        radius = radius.strip('≈') 
        diameter = float(radius) * 2                #process data so as to remove datapoints that arent needed
        csv_data.append([name_moon,name_planet,diameter])
print(csv_data)




