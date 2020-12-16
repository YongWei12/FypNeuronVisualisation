# This code should rotate the vector 

import numpy as np
from numpy import linalg as LA
from numpy.linalg import inv

# create functions for G 
# A and B are vectors 
def GG(A, B):
    return np.array([[np.dot(A,B), -LA.norm(np.cross(A,B)), 0],
            [LA.norm(np.cross(A,B)), np.dot(A,B), 0  ],
            [0, 0, 1]])

# Getting the FF vector 
def FF(A, B):
    return np.array([A, (B-np.dot(A,B)*A)/LA.norm(B-np.dot(A,B)*A) ,  np.cross(B,A)])


#Define vector for UU
def UU(Fi, G ):
    return  np.matmul(np.matmul(Fi,G), inv(Fi))

a= np.array([ 1, 0, 0])
b= np.array([   0,  1, 0])
print(a)
print(GG(a, b))
print(FF(a,b))
print(UU(FF(a,b), GG(a,b)))