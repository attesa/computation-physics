import matplotlib.pyplot as plt
import math
import numpy as np
from fft import fft, fft_power,ifft



filename = "p3data"
file = open(filename, "r")
lines = file.readlines()
T=[]
m=[]


for line in lines:
    if line !='\n' :
        words = line.split()
        mv,tv = [float(s) for s in words]
        T.append(tv)
        m.append(mv)


#N=len(m)
#log2N = math.log(N,2)
#if log2N - int(log2N) > 0.0 :
#    print 'Padding with zeros!'
#    pads = [0.0] * (pow(2, int(log2N)+1) - N)   #now paddle with 0s
#    ma = m + pads

#    N = len(m)
#    print len(m)
#M = fft(ma)



#maxfreq = 15
# Now smooth the data
#for i in range(maxfreq, len(M)-maxfreq ) :
#    M[i] = complex(0,0)
T1=[]
m1=[]
T2=[]
m2=[]

for i in range(len(T)):
    if T[i] < 2.25:
        T1.append(T[i])
        m1.append(m[i])
    elif T[i]>2.28 and T[i]<2.4:
        T2.append(T[i])
        m2.append(m[i])        
        




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

#mp = ifft(M)

#mpr = real(mp)

#mf = mpr[0:len(m)]

fit1 = least_squares_fit(T1, m1)
fit2 = least_squares_fit(T2, m2)

print fit2

plt.scatter(T,m)
plt.xlabel('Temperature')
plt.ylabel('m')
t=np.arange(2,2.5,0.01)
t1=np.arange(2,2.5,0.01)
plt.plot(t,fit1[1]*t+fit1[0])
plt.plot(t1,fit2[1]*t1+fit2[0])


plt.show()
