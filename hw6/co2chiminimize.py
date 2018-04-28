#This program is going to minimize chi-square for Co2, and compared to that of polyfit
#A quadratic fit will be used, AKA, y=ax^2+bx+c
#Han Wen
from cpt import *
import math
import matplotlib.pyplot as plt
import numpy as np


#Read data and store in x and y list, x for year y for ppm
file_name = "co2_mm_mlo.txt"
file = open(file_name, "r")
lines = file.readlines()
file.close()

x=[]
y=[]
for line in lines:
    if len(line) > 4:
        try:
            year = int(line[0:4])
            if year > 1957 and year < 2013:
                words = str.split(line)
                ppm = float(words[4])
                y.append(ppm)
                date=float(words[2])-1957.0
                x.append(float(date))                               #to avoid precission loss, choose years-1957 as x
        except ValueError:
            pass


#Using thress points to have a resonable guess
print x[1],y[1],x[10],y[10],x[100],y[100]
m = Matrix(3,3)
m[0][0]=x[1]**2
m[0][1]=x[1]
m[0][2]=1
m[1][0]=x[10]**2
m[1][1]=x[10]
m[1][2]=1
m[2][0]=x[100]**2
m[2][1]=x[100]
m[2][2]=1

w=Matrix(3,1)
w[0][0]=y[1]
w[1][0]=y[10]
w[2][0]=y[100]
msave=Matrix_copy(m)
abc=Matrix_copy(w)
solve_Gauss_Jordan(m,abc)
print abc



def chisquare(p):
    a=p[0]
    b=p[1]
    c=p[2]
    sum=0.0
    for i in range(len(y)):
        sum += (y[i]-a*x[i]**2-b*x[i]-c)**2      
    return 1.0*0.0001*sum                                       #sigma=1 for all i

def df(p):
    a=p[0]
    b=p[1]
    c=p[2]
    dfda=0.0
    dfdb=0.0
    dfdc=0.0
    for i in range(len(y)):
        dwhole=(y[i]-a*x[i]**2-b*x[i]-c)
        dfda += dwhole*(-x[i]**2)
        dfdb += dwhole*(-x[i])
        dfdc += dwhole*(-1.0)
    return np.array([dfda*0.01*2.0,dfdb*0.01*2.0,dfdc*0.01*2.0])

p=[abc[0][0],abc[1][0],abc[2][0]]                #a,b,c
print abc[0][0],abc[1][0],abc[2][0]
#p=[0.001197,0.785956,313.268]
print df(p),chisquare(p)
iterations = 0
gtol=0.000001                      #accuracy
res = scipy.optimize.fmin_bfgs(f=chisquare, fprime=df,x0=p, gtol=gtol,norm=1000)
print res
print res [0]
print res[1]
print res[2]

#plot poly fit
file_name = "co2_polyfit_output_python.txt"
file = open(file_name, "r")
lines = file.readlines()
file.close()
pz=[]
px=[]
py=[]
for line in lines:
    if len(line) > 4:
        try:
            year = int(line[0:4])
            if year > 1957 and year < 2014:
                words = str.split(line)
                ppm = float(words[1])
                py.append(ppm)
                pz.append(float(words[2]))
                px.append(float(words[0]))                               #to avoid precission loss, choose years-1957 as x
        except ValueError:
            pass

plt.subplot(2, 1, 1)
plt.plot( x, y )
plt.xlabel('BFGS                  Year-1953')
plt.ylabel('CO2(ppm)')
t=np.arange(0,58,0.01)
plt.plot(t,res[0]*t**2+res[1]*t+res[2])  
#plt.plot(t,0.0119696*t**2+0.786*t+313.269)  

plt.subplot(2, 1, 2)
plt.plot( px, py )
plt.xlabel('POLY FIT            Year')
plt.ylabel('CO2(ppm)')
plt.plot(px,pz)
plt.show()

