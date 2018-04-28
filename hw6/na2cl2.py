from nacl import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

name="Na2Cl2"       # for output files
nNa = 3
nCl = 3
n = nNa + nCl
a = 0.2
r_Na = [  [ a, 0, 0 ], [ 3*a, 0, 0] , [5*a,(3**0.5)*a,0] ]
r_Cl = [  [ a, 0.5*a, 0 ], [ -0.5*a, (3**0.5/2)*a, a ] , [0.5*a,a,0]]

#r_Na = [  [ 0, 0, 0 ], [ a, a, 0] ]
#r_Cl = [  [ a, 0, 0 ], [ 0, a, 0 ] ]

#r_Na = [  [0.249 ,  0.367 ,  0.009], [0.249  , 0.901 ,  0.732] ,[0.249  , 0.544   ,0.911],[0.249  , 0.547  , 0.464]]
#r_Cl = [  [0.249 ,  0.435 ,  0.695], [0.249  , 0.801  , 0.511] ,[0.249  , 0.440  , 0.229],[0.249  , 0.788  , 0.950]]

# Initialize the cluster, add guesses at the
# minimum arrangement. 
cluster = Cluster()

for i in xrange(nNa) :
    r = Vector(r_Na[i])
    cluster.add(Na(r))

for i in xrange(nCl) :
    r = Vector(r_Cl[i])
    cluster.add(Cl(r))

print " " + name + " cluster"
print " Initial potential energy = " + str( cluster.potential_energy() )

# Minimize the function
accuracy = 1e-6

res = cluster.minimize( accuracy )

pe = res[1]
iterations = res[4]

# Print out resulting files, and also
# plot the values in matplotlib
print " Minimized potential energy = " + str(pe) + " eV"
print " Binding energy of cluster  = " + str( pe / 3.0 ) + " eV"
print " Number of function calls = " + str( iterations )

file_name = name + ".data"
outfile = open( file_name, 'w' )
for i in xrange( nNa + nCl - 1) :
    for j in range(i+1,nNa+nCl) :
        rij = cluster.ion(i).r - cluster.ion(j).r
        dr = sqrt( np.dot(rij,rij) )
        s =  "(" + cluster.ion(i).name + ")-(" + cluster.ion(j).name + ")"
        print " " + s + " r_" + str(i) + str(j) + " = " + str( dr ) + " nm"

outfile.write( str(cluster) )
outfile.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

[x,y,z] = cluster.convert()
ax.scatter( x,y,z )
plt.show()
