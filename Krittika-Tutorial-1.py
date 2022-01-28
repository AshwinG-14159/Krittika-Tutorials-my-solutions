#tut 1

import csv

l_main = []

def planet_size(l):
    return float(l[2])


with open('tutorials\Tutorial_01\Moons_and_planets.csv','r') as f1:
    r = csv.reader(f1)
    for i in r:
        l_main.append(i)

l_main = l_main[1:]
dict_planets = {}

for i in l_main:
    if i[1] not in dict_planets.keys():
        dict_planets[i[1]] = 0
    dict_planets[i[1]] += 1
    
print(dict_planets)
    
l_main.sort(key = planet_size)
print(l_main)
