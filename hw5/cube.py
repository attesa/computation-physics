from cpt import *
import matplotlib.pyplot as plt

print " Resistant Cube"
print " --------------------------------------"

v0 = 1.0
r1 = 1.0
r2 = 1.0
r3 = 1.0
r4 = 1.0
r5 = 1.0
r6 = 1.0
r7 = 1.0
r8 = 1.0
r9 = 1.0
r10 = 1.0
r11 = 1.0
r12 = 1.0
r12 = 1.0

#the array to record rtotal and r varied
rtt=[]
rv=[]
r10=0.1       # the varied r
#block to calculate rt
for ir in range(100):
    v = Matrix(6, 1)       # column vector with 3 rows
    for i in range(len(v)):
        v[i][0] = v0
    print 'v = '
    print v 

    R = Matrix(6, 6)       # 6x6 resistance matrix
    R[0][0] = 0      # set components using slicing notation
    R[0][1] = 0
    R[0][2] = -r7
    R[0][3] = r7
    R[0][4] = -(r7+r8)
    R[0][5] = r8+r9+r7

    R[1][0] = r6
    R[1][1] = -r6
    R[1][2] = 0
    R[1][3] = 0
    R[1][4] = r6+r9
    R[1][5] = r9

    R[2][0] = r1+r6+r10
    R[2][1] = -(r6+r10)
    R[2][2] = 0
    R[2][3] = 0
    R[2][4] = r6
    R[2][5] = 0       

    R[3][0] = r1
    R[3][1] = (r2+r11)
    R[3][2] = r11
    R[3][3] = 0
    R[3][4] = 0
    R[3][5] = 0 

    R[4][0] = 0
    R[4][1] = r11
    R[4][2] = r3+r11
    R[4][3] = r4
    R[4][4] = 0
    R[4][5] = 0

    R[5][0] = 0
    R[5][1] = 0
    R[5][2] = -(r12+r7)
    R[5][3] = r4+r12+r7
    R[5][4] = -r7
    R[5][5] = r7
    print 'R = '
    print R

    # the solve_Gauss_Jordan replaces R by R^-1 and v by i
    # so save the original R and copy v into a vector i
    R_save = Matrix_copy(R)
    i = Matrix_copy(v)

    solve_Gauss_Jordan(R, i)
    print " Solution using Gauss-Jordan elimination"
    print " i = "
    print i

    i0=i[0][0] + i[3][0] +i[5][0]
    # find the other currents
    print " i_0 = i_1 + i_4 + i_9= " + str(i0)
    rt=v0/i0
    print "r_total="+ str(rt)
    rtt.append(rt)
    rv.append(r10)
    r10=r10+0.5
print rtt,rv
plt.plot(rv,rtt)
plt.show()

# see whether LU decomposition gives the same answer
i = Vector(v)
solve_LU_decompose(R_save, i)
print " Solution using LU Decompositon"
print " i = "
print i

