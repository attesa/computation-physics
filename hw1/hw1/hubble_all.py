#WH_PHY410_HW1_Hubble.py
import math
import matplotlib.pyplot as plt
import numpy as np
# distances in Mpc
r = [ 0.032, 0.034, 0.214, 0.263, 0.275, 0.275, 0.45, 0.5,
      0.5,   0.63,  0.8,   0.9,   0.9,   0.9,   0.9,  1.0,
      1.1,   1.1,   1.4,   1.7,   2.0,   2.0,   2.0,  2.0 ]

# velocities in km/s
v = [ +170, +290, -130, -70,  -185, -220, +200, +290,
      +270, +200, +300, -30,  +650, +150, +500, +920,
      +450, +500, +500, +960, +500, +850, +800, +1090 ]

n=len(r)               #to read the number of sets of data

if n <= 2 :
      print 'Error! Need at least two data points!'
      exit()
#set needed quantities
s_x = 0
s_y = 0
s_xx = 0
s_xy = 0

for i in range(0,n):
    s_x=s_x+r[i]
    s_y=s_y+v[i]
    s_xx=s_xx+r[i]*r[i]
    s_xy=s_xy+r[i]*v[i]
#examine denominator
deno=(n*s_xx)-(s_x)**2
if deno<0.00001:
    print "wrong data, denominator is zeor when doing linear fits"
    exit()
a=(s_xx*s_y-s_x*s_xy)/deno
b=(n*s_xy-s_x*s_y)/deno
#uncertainty
sigma2=0
for i in range(0,n):
    sigma2=sigma2+(v[i]-(a+b*r[i]))**2
if n>2:
    sigma2=sigma2/(n-2)  
    sigma=math.sqrt(sigma2)
    sigma_a=math.sqrt(sigma**2*s_xx/deno)
    sigma_b=math.sqrt(sigma**2*n/deno)
else:
    sigma=0
    sigma_a=0
    sigma_b=0
#plot commands
plt.scatter(r,v)
t=np.arange(r[0],r[n-1],0.001)
plt.plot(t,b*t+a)

# Print out results
print ' Least squares fit of', n, 'data points'
print ' -----------------------------------'
print " Hubble's constant slope   b = {0:6.2f} +- {1:6.2f}  km/s/Mpc".format( b, sigma_b)
print " Intercept with r axis     a = {0:6.2f} +- {1:6.2f}  km/s".format( a, sigma_a)
print ' Estimated v error bar sigma =', round(sigma, 1), 'km/s'

plt.show()




    
    
