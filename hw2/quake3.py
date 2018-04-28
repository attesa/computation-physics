import math
import matplotlib.pyplot as plt
import numpy as np

# define a function to linear fit x-y data without error bars
def least_squares_fit(x, y):
    """Perform a least-squares fit to data (x,y)

    Args :
       x : x values
       y : y values

    Returns :
       a : intercept
       b : slope
       sigma : total uncertainty (sqrt(variance/(n-2)))
       sigma_a : uncertainty on a
       sigma_b : uncertainty on b

    """
    n = len(x)
    s_x  = sum(x)
    s_y  = sum(y)
    s_xx = sum(x_i**2 for x_i in x)
    s_xy = sum(x[i]*y[i] for i in range(n))
    denom = n * s_xx - s_x**2
    if abs(denom) > 0.00001 : 
        a = (s_xx * s_y - s_x * s_xy) / denom
        b = (n * s_xy - s_x * s_y) / denom
        variance = sum((y[i] - (a + b*x[i]))**2 for i in range(n))
        sigma = math.sqrt(variance/(n-2))
        sigma_a = math.sqrt(sigma**2 * s_xx / denom)
        sigma_b = math.sqrt(sigma**2 * n / denom)
        return [a, b, sigma, sigma_a, sigma_b]
    else :
        print 'error : divided by zero!'
        return None



"""Plot data for the Gutenberg-Richter Model.

Here, we plot the curve of the number of earthquakes
greater than magnitude M, for each M value.

So, we loop over the earthquakes, and store the
frequency of each magnitude. At the end of the loop,
we compute the cumulative distribution such that the
value at magnitude M will be the integral of the frequency
distribution for >= M. This is what the Gutenberg-Richter
Model predicts. 

"""


# data downloaded from http://earthquake.usgs.gov/earthquakes/search/
print ' Earthquake data: Gutenberg-Richter Model'
data_file_name = 'bigfile'
file = open(data_file_name, 'r')
lines = file.readlines()
file.close()
print ' read', len(lines), 'lines from', data_file_name

# store event data in two ways for demonstration
# 1. in a python dictionary object with
#    key = magnitude starting in column 50
#    value = number of events with this magnitude
# 2. keeping a "tuple" of the results for later usage with matplotlib
histogram = dict()
magvalues = []
for line in lines:
    if line[0] == '1':  
        try:
            words = line.split(' ')
            mag= float(words[3])
            magvalues.append( mag )
            # For debugging : 
            #print 'read : {0:s} , ({1:6.3f},{2:6.3f}), d = {3:4.1f}, m = {4:6.3f}'.format(
            #    words[0], latitude, longitude, depth, mag
            #    )
            histogram[mag] += 1
        except KeyError : 
            histogram.setdefault(mag, 1)
        except ValueError:
            print 'bad data:', line

num_events = sum(histogram[M] for M in histogram.keys())
num_bins = len(histogram)
print ' stored', num_events, 'events in', num_bins, 'bins'

# x data = M values sorted in increasing order
# y data = log_10(N) where N = number of events with magnitude >= M
M_values = sorted(histogram.keys())
dN_values = [histogram[M] for M in M_values]
log10N_values = [ math.log10(sum(dN_values[i:]))
                  for i in range(len(M_values)) ]
#to obtain a backwards sequence list
mb_values=M_values[::-1]
print mb_values
#obtain the maximum and minimum
maxint=int(mb_values[0])
minint=int(M_values[0])
h=(maxint-minint)/20.0               #step length, totally number is 20
#newm=[7,6.5,6,5.5,5,4.5,4,3.5,1]
newm = [maxint-i*h for i in range(21)]    # new selected m 
#the loop to generate new x,y components
newlogn=[]                                   # corresponding new n


for k in range (len(newm)):
    for j in range(len(mb_values)):
        if newm[k]>=mb_values[j]:
            break
    newlogn.append( log10N_values[-j] )
print newlogn,newm
#The fitting must start from 4
lenm=len(newm)
for m in range(lenm):
    if newm[m] < 4.0:
        for mp in range (m,lenm):
            del newm[m]
            del newlogn[m]
        break
print newm,newlogn


print 'log10N_values is '
for i in xrange(len(log10N_values)) :
    print str(M_values[i]) + '  ' + str(log10N_values[i])
# First plot our "home-grown" values with our least-squares
# fit in place. 
fit = least_squares_fit(newm, newlogn)
print ' least_squares fit to data:'
print ' slope b = {0:6.3f} +- {1:6.3f}'.format( fit[1], fit[4])
print ' intercept a = {0:6.3f} +- {1:6.3f}'.format( fit[0], fit[3])
print ' log_10(N) error bar = {0:6.3f}'.format( fit[2] )
plt.subplot( 2, 1, 1)
#plt.plot( M_values, log10N_values, 'v')
plt.plot( newm, newlogn, 'v')
plt.xlabel( 'Magnitude (M)' )
plt.ylabel( 'log(N)' )
t=np.arange(0,8,0.001)
plt.plot(t,fit[1]*t+fit[0])


# Next also plot matplotlib's version of the same thing.
plt.subplot( 2, 1, 2)
plt.hist( magvalues, bins=90, range=[1.0,10.0], log=True, bottom=0.1,cumulative=-1)
plt.xlabel( 'Magnitude (M)' )
plt.ylabel( 'N' )

# perform a least square fit
#fit = least_squares_fit(M_values, log10N_values)


plt.show()
