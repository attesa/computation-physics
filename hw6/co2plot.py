#This program is going to minimize chi-square for Co2, and compared to that of polyfit
#A quadratic fit will be used, AKA, y=ax^2+bx+c
#Han Wen
from cpt import *
import math
import matplotlib.pyplot as plt
import numpy as np


#Read data and store in x and y list, x for year y for ppm
file_name = "co2_polyfit_output_python.txt"
file = open(file_name, "r")
lines = file.readlines()
file.close()
z=[]
x=[]
y=[]
for line in lines:
    if len(line) > 4:
        try:
            year = int(line[0:4])
            if year > 1957 and year < 2014:
                words = str.split(line)
                ppm = float(words[1])
                y.append(ppm)
                z.append(float(words[2]))
                x.append(float(words[0]))                               #to avoid precission loss, choose years-1957 as x
        except ValueError:
            pass




plt.subplot(2, 1, 1)
plt.plot( x, y )
plt.xlabel('Year')
plt.ylabel('CO2(ppm)')
plt.plot(x,z)
plt.show()
