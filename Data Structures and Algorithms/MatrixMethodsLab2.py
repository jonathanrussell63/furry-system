import numpy as np
import scipy.linalg as la

#EIGENVALUES/VECTORS
A = np.array([[1,0,5],[0,-2,3],[5,3,2]])
eigvals, eigvecs = la.eig(A)
#print(eigvals)
#print(eigvecs)

#SOLVING LINEAR SYSTEM
b = np.array([2,5,-3])
x = np.linalg.solve(A,b)
#print('x=',x)

#SOLVE SYSTEM WITH JACOBI METHOD AND 5 ITERATIONS
#Jacobi method approximates solution to linear equation when
#matrix is diagonally dominant = |diagonal entry| >= |sum of other row entries|
#A = D+L+U = diagonal part + lower triangular + upper triangular
#x_k+1 = D^-1(b-(L+U)x_k) = D^-1(n-Rx)

A = np.array([[3,1,-1], [-1,4,2], [2,0,3]])
b = np.array([7,4,-2])
n = np.size(b)
x = np.array([1,1,1])
D = np.diag(A) #extracts diagonal part of array
R = A-np.diagflat(D) #gets all non-diagonal parts of array
x = np.zeros(len(A[0]))
L= np.triu(A,1)
U = np.tril(A,1)
for i in range(5):
	x = (b-np.dot(R,x))/D
	
	
print(x)

