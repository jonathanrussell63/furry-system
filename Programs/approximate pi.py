import math
import random
def arctanapprox(interations):
	summation=0
	for i in range (0,interations):
		if i%2==0 :
			summation += 1.0/(1+2*i)
		if(i%2==1):
			summation = summation - 1.0/(2*i+1)
	print( summation*4)
	print(4/(2*interations+1))
#very slow convergence
def sumevens(n):
 	sum1=0
 	for i in range (n+1):
 		sum1 += i*2
 	return sum1

def sumofodds(n):
	sum2=0
	for i in range(n):
		sum2+= i*2+1
	return sum2
def fib(n):
	a=1
	b=1
	d=1
	for i in range (n-2):
		c = a+b
		d*=c
		a=b
		b=c
	return d

def wallis(n):
	top=2.0
	bottom=1.0
	halfpi=1
	for i in range(n):
 		if i%2==0 :
 			halfpi *= top/bottom
 			bottom +=2
 			
 		if i%2==1:
 			halfpi*=top/bottom
 			top+=2
 	
	return halfpi

def incircle(r, x,y):
	a=x**2+y**2
	if(a<r**2):
		return True

def montecarlo(n,r):
	counter=0
	for i in range (n):
		a=random.random()*r
		b=random.random()*r
		if(incircle(r,a,b)==True):
			counter= counter +1
	return 4*counter/n

def sumpi(n):
	count =1
	summation=0
	for i in range(n):
		summation+=((-1)**i)*1.0/(count*(3**i))
		count+=2
	return summation*math.pow(12,.5)
#very accurate even at fairly low n

def root(n,r):

	nextone= .5*(1+n/1)
	for i in range(r):
		nexttwo = .5*(nextone+n/nextone)
		nextone=nexttwo
	return nexttwo

def forwardfunc(k,h,function,x):
	code = parser.expr(function).compile()

	a=0
	for i in range(k+1):
		x=x+(k-i)*h
		a=a+((-1)**i)*math.factorial(k)/(math.factorial(i)*math.factorial(k-i))*eval(code)


def wallis2(trials):
	product = 1
	for i in range(1,trials+1):
		product= product * (2*i)/(2*i+1)*(2*i)/(2*i-1) 
	return(product)

product=1
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,81,83]
for i in range(len(primes)):
	product= product*(1+primes[i]**2)/(primes[i]**2-1)
print (product)
