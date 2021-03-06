import math
import matplotlib.pyplot as plt
import numpy as np

def sine_transform(data):
    """Return Fourier sine transform of a real data vector"""
    N = len(data)
    transform = [ 0 ] * N
    for k in range(N):
        for j in range(N):
            angle = math.pi * k * j / N
            transform[k] += data[j] * math.sin(angle)
    return transform

file_name = "co2_mm_mlo.txt"
file = open(file_name, "r")
lines = file.readlines()
file.close()

dates = []
data = []
for line in lines:
    if len(line) > 4:
        try:
            year = int(line[0:4]) 
            if year > 1957 and year < 2013:
                words = str.split(line)
                dates.append(float(words[2]))
                ppm = float(words[5])
                if ppm > 0: data.append(ppm)
        except ValueError:
            pass

print " read", len(data), "values from", file_name


transform = sine_transform(data)

freqs = [ float(i) for i in xrange(len(transform))]

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

whn=int(len(dates)/3)
fit = least_squares_fit(dates, data)
print ' least_squares fit to data:'
print ' slope b = {0:6.3f} +- {1:6.3f}'.format( fit[1], fit[4])
print ' intercept a = {0:6.3f} +- {1:6.3f}'.format( fit[0], fit[3])
print ' log_10(N) error bar = {0:6.3f}'.format( fit[2] )
slope=fit[1]
intercept=fit[0]

fit = least_squares_fit(dates[0:whn], data[0:whn])
print ' least_squares fit to data1:'
print ' slope b = {0:6.3f} +- {1:6.3f}'.format( fit[1], fit[4])
print ' intercept a = {0:6.3f} +- {1:6.3f}'.format( fit[0], fit[3])
print ' log_10(N) error bar = {0:6.3f}'.format( fit[2] )

fit = least_squares_fit(dates[whn:2*whn], data[whn:2*whn])
print ' least_squares fit to data2:'
print ' slope b = {0:6.3f} +- {1:6.3f}'.format( fit[1], fit[4])
print ' intercept a = {0:6.3f} +- {1:6.3f}'.format( fit[0], fit[3])
print ' log_10(N) error bar = {0:6.3f}'.format( fit[2] )

fit = least_squares_fit(dates[2*whn:3*whn], data[2*whn:3*whn])
print ' least_squares fit to data3:'
print ' slope b = {0:6.3f} +- {1:6.3f}'.format( fit[1], fit[4])
print ' intercept a = {0:6.3f} +- {1:6.3f}'.format( fit[0], fit[3])
print ' log_10(N) error bar = {0:6.3f}'.format( fit[2] )

plt.subplot(2, 1, 1)
plt.plot( dates, data )
plt.xlabel('Year')
plt.ylabel('CO2(ppm)')
t=np.arange(1958,2013,0.01)
plt.plot(t,slope*t+intercept)


ax = plt.subplot(2, 1, 2)
plt.plot( freqs, transform )
ax.set_yscale('log')

plt.show()
