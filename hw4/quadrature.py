from trapezoid import *
from simpson import *
from math import *
import matplotlib.pyplot as plt 


#true=exp(1.0)-1.0
#print true
#while n1 % 2 != 0 :
#   n1 = int(raw_input( "Enter number of intervals desired for trapezoidal rule (must be even)" ))

n=[]
d1=[]
d2=[]

for n1 in range(100,1100,100):
    a = 0.0
    b = 1.0
    ans1 = trapezoid(exp, a, b, n1)
    diff1=abs(true-ans1)
    print 'Trapezoidal rule = ' + str(ans1)
    print 'Difference between the result and the true value:' ,diff1
    d1.append(diff1)

    ans2 = simpson(exp, a, b, n1)
    print 'Simpson = ' + str(ans2)
    diff2=abs(true-ans2)
    print diff2
    d2.append(diff2)
    n.append(n1)
dl1=[]
dl2=[]    
for x in d1:
    dl1.append(log10(x))
for y in d2:
    dl2.append(log10(y))
    

p1,=plt.plot(n,d1)
p2,=plt.plot(n,d2)
plt.legend ([p1,p2],["trapezoid","simpson"])
plt.yscale('log')
plt.show()
