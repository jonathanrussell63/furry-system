import numpy as np
# part a
def forwardsub(L, b):
	n = len(L)
	#by forward substitution:
	#x_i = b1/a11 if i=1,
	#      a1/(aii)(bi- sum_j=1 ^(i-1) a_ij x_j) if i!=1
	x = []
	for i in range(n):
		if i==0:
			x.append(b[0]/L[0][0])
		else:
			summation  = 0
			for j in range(i):
				summation += L[i][j] * x[j]
			x.append(1/L[i][i] * (b[i]-summation))

	return x

# part b
L = []
for i in range(1,6):
	line = []
	for j in range(1,6):
		if i>=j:
			line.append(i+j*j)
		else:
			line.append(0)
	L.append(line)

b = [1,4,9,16,25]

print("Matrix L=",L)
print("Matrix b=",b)
print()

print("x = ",forwardsub(L,b))
print()

# part c
L = np.array(L)
b = np.array(b)
c = L.dot(forwardsub(L,b))

print("Lx=",c)