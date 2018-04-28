import math
import random
import matplotlib.pyplot as plt
from cpt import *

class Ising :
    def __init__(self, J=1.0, L=10, N=100, T=2., H=0.) : 

        self.J = J                       # spin-spin coupling += ferro, -= antiferro
        self.L_x = L; self.L_y = L       # number of spins in x and y
        self.N = N                       # total number of spins
        self.s = []                      # L_x x L_y array of spin values
        self.T = T                       # Temperature
        self.H = H                       # magnetic field

        self.w = []                      # Boltzmann factors at fixed T and H
        self.steps = 0                   # Monte Carlo steps so far
        self.acceptance_ratio = 0        # accepted steps / total number of steps

        # create spin lattice and set spin randomly up or down (hot start)
        for i in range(self.L_x):
            self.s.append( [ ] )
            for j in range(self.L_y):
                self.s[i].append(random.choice( (-1, 1) ))
        self.compute_Boltzmann_factors()
        self.steps = 0



    def compute_Boltzmann_factors(self):
        self.w = []
        for m in range(5):
            self.w.append( [] )
            sum_of_neighbors = -4 + 2 * m
            for n in range(2):
                s_i = -1 + 2 * n
                factor = math.exp( -2.0 * (self.J * sum_of_neighbors + self.H) * s_i / self.T )
                self.w[m].append(factor)



    def Metropolis_step_accepted(self):

        # choose a random spin
        i = random.randrange(self.L_x)
        j = random.randrange(self.L_y)

        # find the sum of neighbors assuming periodic boundary conditions
        sum_of_neighbors = ( self.s[(i-1)%self.L_x][j] + self.s[(i+1)%self.L_x][j] +
                             self.s[i][(j-1)%self.L_y] + self.s[i][(j+1)%self.L_y] )

        # access ratio of precomputed Boltzmann factors,
        ratio = self.w[2 + int(sum_of_neighbors/2)][int((1 + self.s[i][j])/2)]

        # apply the Metropolis test
        if ratio > 1.0 or ratio > random.random():
            self.s[i][j] = -self.s[i][j]
            return True
        else:
            return False

    

    def one_Monte_Carlo_step_per_spin(self):
        accepts = 0
        for n in range(self.N):
            if self.Metropolis_step_accepted():
                accepts += 1
        self.acceptance_ratio = accepts / float(self.N)
        self.steps += 1

    def magnetization_per_spin(self):

        s_sum = 0.0
        for i in range(self.L_x):
            for j in range(self.L_y):
                s_sum += self.s[i][j]
        return s_sum / float(self.N)

    def energy_per_spin(self):

        s_sum = 0.0
        ss_sum = 0.0
        for i in range(self.L_x):
            for j in range(self.L_y):
                s_sum += self.s[i][j]
                ss_sum += self.s[i][j] * (self.s[(i+1)%self.L_x][j] + self.s[i][(j+1)%self.L_y])
        return -(self.J * ss_sum + self.H * s_sum) / float(self.N)

print " Two-dimensional Ising Model - Metropolis simulation"
print " ---------------------------------------------------"
L = int(input(" Enter number of spins L in each direction: "))
#T = float(input(" Enter temperature T: "))
H = float(input(" Enter magnetic field H: "))
MC_steps = int(input(" Enter number of Monte Carlo steps: "))


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

Tout=[]
mav=[]
eav=[]
hcout=[]
T=2.0
Nl=50
Th=0.01
fp=open("p3data","w")
for count in range(Nl):
    print count
    ising = Ising(L=L, N=L*L, T=T, H=H)

    therm_steps = int(0.2 * MC_steps)


    print " Performing", therm_steps, "thermalization steps ..."
    for i in range(therm_steps):
        ising.one_Monte_Carlo_step_per_spin()

    print " Done ... Performing production steps ..."
    m_av = 0.0; m2_av = 0.0; e_av = 0.0; e2_av = 0.0
    #data_file = open("isingT.data", "w")
    for i in range(MC_steps):
        ising.one_Monte_Carlo_step_per_spin()
        m = ising.magnetization_per_spin()
        e = ising.energy_per_spin()
        m_av += m
        m2_av += m**2
        e_av += e
        e2_av += e**2
        #data_file.write(repr(m) + "\t" + repr(e) + "\n")
    #data_file.close()
    print " M/spin and E/spin values written in isingT.data"
    m_av /= float(MC_steps)
    m2_av /= float(MC_steps)
    e_av /= float(MC_steps)
    e2_av /= float(MC_steps)
    mav.append(abs(m_av))
    eav.append(e_av)
    Tout.append(T)
    s = '{0:8.4f} {1:8.4f}\n'.format(T,abs(m_av))
    fp.write(s)
    T += Th
#    if count==1 :
#        c = (eav[1]-eav[0])/Th
#        print c
#        hcout.append(c)                               #hcout[0]
#    elif count>1 and count < Nl-1:
#        c = (eav[count]-eav[count-2])/Th*2
#        print c
#        hcout.append(c)                               #hcout[count-1]
#    elif count == Nl-1:
#        c = (eav[count]-eav[count-2])/Th*2
#        print c
#        hcout.append(c)
#        c = (eav[count]-eav[count-1])/Th
#        print c
#        hcout.append(c)                               #hcout[N-1] hcout[N-2]              
#print " <m> =", m_av, "+/-", math.sqrt(m2_av - m_av**2)
#print " <e> =", e_av, "+/-", math.sqrt(e2_av - e_av**2)
#print ising.w


print Tout,len(Tout)
print mav,len(mav)
#print hcout,len(hcout)
#plt.subplot(2, 1, 1)
plt.plot(Tout,mav)
plt.xlabel('Temperature')
plt.ylabel('m')

#plt.subplot(2,1,2)
#plt.plot(Tout,hcout)
#plt.xlabel('Temperature')
#plt.ylabel('heat capacity')

plt.show()
