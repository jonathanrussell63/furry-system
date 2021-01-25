import numpy as np
import random
from numpy import linalg as LA
import math

#4a - creating a random matrix with values from 0 to 1
array = []
for i in range(5):
	array.append([])
	for j in range(5):
		array[i].append(random.random())
array = np.array(array)

#displaying the array
print("Matrix A: ",array)
#verifying it is 5x5
print(array.shape)

#w is a vector of eigenvalues, v is the matrix of eigen vectors as the columns
w,v = LA.eig(array)
print()
#4b - D is the matrix of eigenvalues along the diagonal
D = np.diag(w)
#v_1 is the inverse of the matrix of eigenvectors
v_1 = np.linalg.inv(v)
#when subtracting, both imaginary and real parts of the matrix values are of the magnitude 10^-17 or so. This matrix is essentially the zero matrix.
print("X^-1DX-A:",(v.dot(D)).dot(v_1)-array)