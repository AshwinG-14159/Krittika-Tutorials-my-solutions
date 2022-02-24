#tut 1
''' 
This tut deal with the basics of python itself

Given: In the file Moons_and_planets.csv, we can find the names of the moons of each planet as well as the planet they orbit

Task: Find the number of moons of each planet
Order the moons (along with their planets) according to their sizes


'''
import csv

l_main = []

def planet_size(l): #returns the size of the planet, given complete list of data on the planet
    return float(l[2])


#csv file open and read into list l_main
with open('tutorials\Tutorial_01\Moons_and_planets.csv','r') as f1:
    r = csv.reader(f1)
    for i in r:
        l_main.append(i)

l_main = l_main[1:] #ignoring headings
dict_planets = {}

for i in l_main:   # creating dictionary with planets and number of moons
    if i[1] not in dict_planets.keys():
        dict_planets[i[1]] = 0
    dict_planets[i[1]] += 1
    
print(dict_planets) # prints dictionary with planet names and number of moons
    
l_main.sort(key = planet_size) #sorts moon data by planet size
print(l_main) 
