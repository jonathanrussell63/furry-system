# f(x)=x^3-3*x+1 in [0,1]

eps=.001
p1=0
p2=1
f1 = p1**3-3*p1+1
f2 = p2**3-3*p2+1
itr=0
while (p2-p1)/2>=eps:
	x = (p1+p2)/2
	fx = x**3-3*x+1
	if fx*f1<0:
		p2=x
	if fx*f2<0:
		p1=x
	itr+=1
	print('iteration', itr)
	print('x=',round(x,3))