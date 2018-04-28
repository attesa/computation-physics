from cpt import *


m1 = 16.0
m2 = 12.0


# Matrix with masses as the diagonal elements
M = Matrix(5,5)
M[0][0] = m1
M[1][1] = m2
M[2][2] = m2
M[3][3] = m2
M[4][4] = m1
print "M = "
Matrix_print(M)

[detM, Minv] = inverse(M)
print "Minv = "
Matrix_print(Minv)


# "Spring" constants affecting each mass
kco = 1.21
kcc = 0.96

K = [
    [   kco,    -kco,       0.0  ,   0.0  ,   0.0   ],
    [   -kco,   kco + kcc,  -kcc  , 0.0 ,      0.0  ],
    [   0.0,    -kcc,       2*kcc  ,  -kcc ,0.0     ],
    [   0.0,    0.0 ,       -kcc  ,  kco + kcc, -kco     ],
    [   0.0,    0.0 ,       0.0   ,  -kco ,  kco     ]
]

print "K = "
Matrix_print(K)




# Solve with generalized eigenvector solution
[ eigenvalues, eigenvectors ] = solve_eigen_generalized(K, M)

print "Eigenvalues ="
print eigenvalues
print "Eigenvectors ="
Matrix_print(eigenvectors)
