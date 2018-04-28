from read_plot import *
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
from matplotlib import legend

#x,y = read_plot("poincare_plot.txt")

filename="bifurcation.data"
file = open( filename, 'r')
lines = file.readlines()
x = []
y = []
for line in lines:
    if line != '\n':
        words = line.split()
        x.append(float(words[0]))
        y.append(float(words[1]))

plt.scatter(x,y)


plt.show()
