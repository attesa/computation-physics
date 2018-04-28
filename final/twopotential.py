#PHY 505 final project, problem 2 part a
#This program is going to plot the gravitational potential for both cases
#Han Wen 2014-12-10


import matplotlib.pyplot as plt
from matplotlib import legend

Gme = 6.67*5.972e13                    #Gravitational constant x mass of earth
Gmm = 6.67*7.348e11                    #Gravitational constant x mass of moon
rem = 384400000.0                        #distance from earth to moon

r_out = []
v_real = []
v_patched = []

N = 10000

dr = rem/N                    #step length
r = 10*dr                        #distance to earth 

for i in range(N-11):
    Ve = -Gme/r
    Vm = -Gmm/(rem-r)
    r_out.append(r)
    if abs(Ve)>abs(Vm):
        v_patched.append(Ve)
    elif abs(Ve)==abs(Vm):
        v_patched.append(Ve)
    else:
        v_patched.append(Vm)
    v_real.append(Ve+Vm)
    r += dr

plt.subplot(2,1,1)
plt.plot(r_out,v_patched)
plt.xlabel("r(m)")
plt.ylabel("V_PATCHED")

plt.subplot(2,1,2)
plt.plot(r_out,v_real)
plt.xlabel("r(m)")
plt.ylabel("V_TRUE")

plt.show()
