import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_plot_3d(filename) :
    """This is a simple function that can be used to
    read in a plot of data from a text file, which
    is separated by newline characters.
    It returns the arrays as x,y

    Args : filename : name of the file

    Returns : x : x values
              y : y values
    
    """
    try: 
        file = open( filename, 'r')
        lines = file.readlines()
        x = []
        y = []
        z = []
        for line in lines :
            if line != '\n' :
                words = line.split()
                ix, iy, iz = [float(s) for s in words]
                x.append( ix )
                y.append( iy )
                z.append( iz )
        return x,y,z
    except:
        print 'Error in read_plot. Returning None'
        return None

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
file = open( "wh_butterfly.txt", 'r')
lines = file.readlines()
x = []
y = []
z = []
for line in lines :
    if line != '\n' :
        words = line.split()
        ix, iy, iz = [float(s) for s in words]
        x.append( ix )
        y.append( iy )
        z.append( iz )


ax.scatter( x,y,z )
plt.show()
