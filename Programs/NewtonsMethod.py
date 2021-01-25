# f(x)=x^3-3x^2+1

eps = .001
x = 1 #initial guess
itr=0
while abs(x**3-3*x**2+1)>=eps:
	x = x-(x**3-3*x**2+1)/(3*x**2-6*x)
	itr +=1
	print('iteration ', itr)
	print('x=',x, 'f(x)=',x**3-3*x**2+1)