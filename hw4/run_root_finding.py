from root_finding import *
from math import *

def fp1 ( x ) :
    return (tan(x))**2+1.0
def fp2 ( x ) :
    return 1.0-(tanh(x))**2



print(" Algorithms for root of tangent")
print(" ------------------------------------------------")
print(" 1. Simple search")
x0 = float ( input(" Enter initial guess x_0 : ") )
dx = float ( input(" Enter step dx : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_simple(tan, x0, dx, acc,1000,True)
print  str ( answer ) + "\n\n"

print(" 2. root tangent")
x0 = float ( input(" Enter initial guess x_0 : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_tangent(tan, fp1, x0, acc,1000,True)
print  str ( answer ) + "\n\n"


print(" Algorithms for root of tanh")
print(" ------------------------------------------------")

print(" 1. Simple search")
x0 = float ( input(" Enter initial guess x_0 : ") )
dx = float ( input(" Enter step dx : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_simple(tanh, x0, dx, acc,1000,True)
print  str ( answer ) + "\n\n"

print(" 2. root tangent")
x0 = float ( input(" Enter initial guess x_0 : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_tangent(tanh, fp2, x0, acc,1000,True)
print  str ( answer ) + "\n\n"
