import numpy as np
import scipy.linalg as la

A = np.array([[3,1,-1],[-1,4,2],[2,0,3]])
b = np.array([7,4,2])
is_dom = True
for i in range(3):
	row_sum =0
	for j in range(3):
		row_sum += abs(A[i,j])
	if row_sum-abs(A[i,i]) > abs(A[i,i]):
		is_dom = False
if is_dom:
	print('A is diagonally dominant')
else:
	print('A is not diagonally dominant')

L= np.tril(A)
U= np.triu(A,1)
L_1 = np.linalg.inv(L)
x = [1,1,1]
count =0
while(np.linalg.norm(A.dot(x)-b)>1/100):
	x = L_1.dot(b-U.dot(x))
	count+=1
	print('iteration: ', count, 'x= ',x)

