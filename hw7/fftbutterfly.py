import matplotlib.pyplot as plt

from fft import fft, fft_power, ifft
from numpy import array, real
import math
import time



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
file.close()
        



#fft part
N = len(x)
log2N = math.log(N, 2)
if log2N - int(log2N) > 0.0 :
    print 'Padding with zeros!'
    pads = [0.0] * (pow(2, int(log2N)+1) - N)
    x = x + pads
    y = y + pads
    z = z + pads
    N = len(x)
    print len(y)

X = fft(x)
Y = fft(y)
Z = fft(z)
t = []
for i in range(len(X)):
    t.append(i)
#Yre = [math.sqrt(Y[i].real**2+Y[i].imag**2) for i in xrange(len(Y))]
#powery = fft_power(Y)
#powerx = array([ float(i) for i in xrange(len(powery)) ] )

ax1 = plt.subplot(1, 1, 1)
#p1, = plt.plot( x, y )
#p2, = plt.plot( x, ysmoothedreal )
p1, = plt.plot( t, X )
ax1.legend( [p1], ['Z fft'] )

#ax2 = plt.subplot(3, 1, 2)
#p3, = plt.plot( t, X )
#ax2.legend( [p3], ["X fft"] )

#ax3 = plt.subplot(3, 1, 2)
#p4, = plt.plot( t, Z )
#ax3.legend( [p4], ["Z fft"] )
plt.show()
