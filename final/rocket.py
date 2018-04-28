# balle - Program to compute the trajectory of a baseball
#         using the Euler method.
# Adapted from Garcia, Numerical Methods for Physics, 2nd Edition

#* Set initial position and velocity of the baseball


#Modified by Han Wen for final project
#2014-12-09
from math import *




#y1 = 0.0
speed = 0.0
#theta = 0.0
r1 = [0.0] * 2
v1 = [0.0] * 2
r =  [0.0] * 2
v =  [0.0] * 2
accel = [0.0] * 2
radius_e = 6371000.0                 #radius of the earth


euler = 0
#y1 = input( "Enter initial height (meters): ")
r1[0] = 0
r1[1] = radius_e          #y1     # Initial vector position
#speed = input( "Enter initial speed (m/s): ")
#theta = input("Enter initial angle (degrees): ")

v1[0] = 0          #speed*cos(theta*pi/180.)   # Initial velocity (x)
v1[1] = 0          #speed*sin(theta*pi/180.)   # Initial velocity (y)
r[0] = r1[0]
r[1] = r1[1]       # Set initial position and velocity
v[0] = v1[0]
v[1] = v1[1]             


def Gravitational_acceleration(r):
    return (6.67*5.97*10**13)/r**2
    

def rho(r):
    a = 1.2*exp(-r/10000.0)
    return a




#* Set physical parameters (mass, Cd, etc.)
F = 34020000.0   # force of thrust 
B = 17212.0      #coefficient of mass decreasing
Cd = 0.35      # Drag coefficient (dimensionless)
area = 25.0  # Cross-sectional area of projectile (m^2)
#grav = 9.81    # Gravitational acceleration (m/s^2)
mass = 2970000.0   # Mass of projectile (kg)
airFlag = 0
#rho = 0.0
airFlag = input( "Air resistance? (Yes:1, No:0): ")
if airFlag == 0 :
    rho_c = 0      # No air resistance
else :
    rho_c = 1    # Density of air (kg/m^3)
#air_const = -0.5*Cd*rho*area/mass  # Air resistance constant

euler = input("Use Euler (0), Euler-Cromer (1), or Midpoint(2) ? ")

#* Loop until ball hits ground or max steps completed
tau = 0.0
tau = input("Enter timestep, tau (sec): ")
#iStep = 0
maxStep = int(165/tau)   # Maximum number of steps
tplot = []
yplot = []
accplot = []
vplot = []
#tNoAir = []
#yNoAir = []
t = 0.0
for iStep in xrange(maxStep) :

    #print iStep
    #* Record position (computed and theoretical) for plotting
    tplot.append( t )   # Record trajectory for plot
    yplot.append( r[1]-radius_e )
    vplot.append(v[1])
    t += tau     # Current time, +save more time than * 
#    xNoAir.append( r1[0] + v1[0]*t )
#    yNoAir.append( r1[1] + v1[1]*t - 0.5*grav*t*t )

    #* Calculate the acceleration of the ball 
#    normV = sqrt( v[0]*v[0] + v[1]*v[1] )



    air_const = -0.5*Cd*rho_c*rho(r[1]-radius_e)*area/mass        
#    accel[0] = air_const*normV*v[0]   # Air resistance
    accel[1] = air_const*v[1]*v[1]  # Air resistance
    accel[1] -= Gravitational_acceleration(r[1])               # Gravity
    accel[1] += F/mass
    accplot.append(accel[1])
    mass -= B*tau


    #* Calculate the new position and velocity using Euler method
    if ( euler == 0 ) :        # Euler step
#        r[0] += tau*v[0]                 
        r[1] += tau*v[1]                 
#        v[0] += tau*accel[0]     
        v[1] += tau*accel[1]     
    elif ( euler == 1 ) : # Euler-Cromer step
#        v[0] += tau*accel[0]     
        v[1] += tau*accel[1]     
#        r[0] += tau*v[0]                 
        r[1] += tau*v[1]                 
    else :                   # Midpoint step
#        vx_last = v[0]
        vy_last = v[1]
#        v[0] += tau*accel[0]     
        v[1] += tau*accel[1]     
#        r[0] += tau*0.5*(v[0] + vx_last)                 
        r[1] += tau*0.5*(v[1] + vy_last)


        #* If ball reaches ground (y<0), break out of the loop
#        if r[1] < 0 :
#            xplot.append( r[0] )  # Record last values computed
#            yplot.append( r[1] )
#            break                  # Break out of the for loop


#    print "a"
#    print r[1]
#    print v[1]
#    print accel[1]
#* Print maximum range and time of flight
print "Maximum range is " + str( r[1] ) + " meters"
print "the final speed is" + str(v[1])
#print "Time of flight is " +str( iStep*tau ) + " seconds"
print accel[1]
print air_const*v[1]*v[1]
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
from matplotlib import legend


ax1 = plt.subplot(2,1,1)

p1, = ax1.plot(tplot,yplot)
#p2, = ax1.plot(xNoAir,yNoAir)
plt.xlabel("time(s)")
plt.ylabel("Height(m)")
plt.subplot(2,1,2)
plt.plot(tplot,vplot)
#ax1.legend([p1, p2], ["Numerical", "Exact (no air)"])
plt.xlabel("time(s)")
plt.ylabel("Velocity(m/s)")
plt.show()
