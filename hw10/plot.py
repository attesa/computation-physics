import matplotlib.pyplot as plt
import math
from numpy import array, real
from fft import fft, fft_power,ifft

filename = "l100.data"
file = open(filename, "r")
lines = file.readlines()
T=[]
m=[]
c=[]

for line in lines:
    if line !='\n' :
        words = line.split()
        tv,mv,cv = [float(s) for s in words]
        T.append(tv)
        m.append(mv)
        c.append(cv)

N=len(m)
log2N = math.log(N,2)
if log2N - int(log2N) > 0.0 :
    print 'Padding with zeros!'
    pads = [0.0] * (pow(2, int(log2N)+1) - N)   #now paddle with 0s
    ma = m + pads
    ca = c + pads
    N = len(m)
    print len(m)
M = fft(ma)
C = fft(ca)


maxfreq = 15
# Now smooth the data
for i in range(maxfreq, len(M)-maxfreq ) :
    M[i] = complex(0,0)
    C[i] = complex(0,0)

cp = ifft(C)
mp = ifft(M)
cpr = real(cp)
mpr = real(mp)

mf = mpr[0:len(m)]
cf = cpr[0:len(c)]


plt.subplot(2, 1, 1)
plt.plot(T,mf)
plt.xlabel('Temperature')
plt.ylabel('m')

plt.subplot(2,1,2)
plt.plot(T,cf)
plt.xlabel('Temperature')
plt.ylabel('heat capacity')

plt.show()
