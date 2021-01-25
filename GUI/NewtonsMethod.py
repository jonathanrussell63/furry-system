#f(x)=x^2-2

x=1

for i in range(10):
	x= (x**2+2)/(2*x)
	print('Iteration: ', i+1)
	print('x = ', x)

