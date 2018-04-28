import math
import random
import cpt
import matplotlib.pyplot as plt
import numpy as np

print " Random walk in 1 dimension"
print " --------------------------"
n_walkers = int(input(" Enter number of walkers: "))
n_steps = int(input(" Enter number of steps: "))

# walker positions initialized at x = 0  y=0
x = [ 0.0 ] * n_walkers
y = [ 0.0 ] * n_walkers
z = [ 0.0 ] * n_walkers

steps = [ 0.0 ] * n_steps       # to save step number i (time)
x2ave = [ 0.0 ] * n_steps       # to accumulate x^2 values
sigma = [ 0.0 ] * n_steps        # to accumulate fluctuations in x^2
x2in = cpt.Matrix(n_walkers,n_steps)       # individual x^2+y^2

# loop over walkers
for walker in range(n_walkers):

    # loop over number of steps
    for step in range(n_steps):

        # take a random step
        x[walker] += random.choice( (-1, 1) )
        y[walker] += random.choice( (-1, 1) )
        z[walker] += random.choice( (-1, 1) )
        #while x[walker]**2+y[walker]**2 >= 1:
        #    x[walker] += random.choice( (-1, 1) )
        #    y[walker] += random.choice( (-1, 1) )            
        # accumulate data
        steps[step] = step + 1.0
        x2ave[step] += x[walker]**2 + y[walker]**2 + z[walker]**2 
        x2in[walker][step] = x[walker]**2 + y[walker]**2 + z[walker]**2

# average the squared displacements and their variances
for step in range(n_steps):
    x2ave[step] /= float(n_walkers)
#    sigma[step] /= float(n_walkers)

#calculate uncertainty in each step
for step in range(n_steps):
    for walker in range(n_walkers):
        sigma[step] += (x2in[walker][step]-x2ave[step])**2
    if sigma[step] == 0.0:      # happens for first step!
        sigma[step] = 1.0
    if n_walkers > 1:
        sigma[step] = math.sqrt(sigma[step]/(n_walkers*(n_walkers - 1.0)))    



# fit data to a straight line
a, b, sigma_a, sigma_b, chisqr = cpt.chi_square_fit(steps, x2ave, sigma)
print " Fit to straight line <x^2> = a + b n"
print " Intercept a = " + repr(a) + " +- " + repr(sigma_a)
print " Slope     b = " + repr(b) + " +- " + repr(sigma_b)
print " Chisqr/dof  = " + repr(chisqr / (n_steps - 2.0))

# store in file for plotting
file = open("rwalk.data", "w")
for step in range(n_steps):
    file.write(repr(steps[step]) + "\t" + repr(x2ave[step]) +
                    "\t" + repr(sigma[step]) + "\n")
file.close()
print " t, <x^2>, sigma in file rwalk.data"

plt.scatter(steps, x2ave )
t=np.arange(-100,n_steps+100,0.1)
plt.plot(t,b*t+a)

#plt.scatter( [i for i in range(len(steps))], steps )


plt.show()
