from root_finding import *
from math import *


def fp2 ( x ) :
    return 1.0-(tanh(x))**2



print(" 2. root tangent")
x0 = float ( input(" Enter initial guess x_0 : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_tangent(tanh, fp2, x0, acc,1000,True)
print  str ( answer ) + "\n\n"
