from nacl import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

#I am going to use the random initial coordinates to generate random models.
#comparing energy and save new configurations.
name="Na4Cl4"       # for output files
nNa = 4
nCl = 4
n = nNa + nCl
a = 0.23                    #The equilibrium distance


#file_name = name + ".data"
#outfile = open( file_name, 'w' )

#Enmin = []                  #array to store new minimum energy 
#Enmin.append(10000.0)       #Giving a big number to start   
#r_Na = [  [ 0, 0, 0 ], [ 1.5*a, (3**0.5/2)*a, 0] , [0,(3**0.5)*a,0] ]
#r_Cl = [  [ a, 0, 0 ], [ -0.5*a, (3**0.5/2)*a, 0 ] , [a,(3**0.5)*a,0]]

#r_Na = [  [ 0, 0, 0 ], [ a, a, 0] ]
#r_Cl = [  [ a, 0, 0 ], [ 0, a, 0 ] ]

r_Na = [  [ 0, 0, 0 ], [ 1.5*a, (3**0.5/2)*a, 0] , [0,(3**0.5)*a,0], [0,0,0] ]
r_Cl = [  [ 0, 0, 0 ], [ -0.5*a, (3**0.5/2)*a, 0 ] , [a,(3**0.5)*a,0], [0,0,0]]
for im in range(300):
    #define a random initial for both Nas and Cls
    for vec in r_Na:
        for iv in range(3):
            vec[iv]=random.random()
    for vec in r_Cl:
        for iv in range(3):
            vec[iv]=random.random()
    # Initialize the cluster, add guesses at the
    # minimum arrangement. 
    cluster = Cluster()

    for i in xrange(nNa) :
        r = Vector(r_Na[i])
        cluster.add(Na(r))

    for i in xrange(nCl) :
        r = Vector(r_Cl[i])
        cluster.add(Cl(r))

#    print " " + name + " cluster"+str(random.random())
#    print " Initial potential energy = " + str( cluster.potential_energy() )

    # Minimize the function
    accuracy = 1e-7

    res = cluster.minimize( accuracy )

    pe = res[1]
    iterations = res[4]
    #determine if it's exist in array
#    for energy in Enmin:


    # Print out resulting files, and also
    # plot the values in matplotlib
    print " Minimized potential energy = " + str(pe) + " eV"
    #outfile.write( " Minimized potential energy = " + str(pe) + " eV")
    #print " Binding energy of cluster  = " + str( pe / 2.0 ) + " eV"
    #print " Number of function calls = " + str( iterations )

    for i in xrange( nNa + nCl - 1) :
        for j in range(i+1,nNa+nCl) :
            rij = cluster.ion(i).r - cluster.ion(j).r
            dr = sqrt( np.dot(rij,rij) )
            s =  "(" + cluster.ion(i).name + ")-(" + cluster.ion(j).name + ")"
            print " " + s + " r_" + str(i) + str(j) + " = " + str( dr ) + " nm"
    print str(cluster)
#    outfile.write( str(cluster) )
#outfile.close()

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#[x,y,z] = cluster.convert()
#ax.scatter( x,y,z )
#plt.show()
