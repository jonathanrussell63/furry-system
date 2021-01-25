import parser
import math
from math import sin
from math import cos
from math import tan
#formula = "sin(x)*x**2"
#code = parser.expr(formula).compile()

#for i in range (0,20):
#	for j in range (0,10):
#		x=i+j*.1
#		summation+=eval(code)*.1

#print(summation)
#successful LEFT HAND reimann sum.
def leftreimannsum(function, lower_bound, upper_bound, increments):
	summation=0
	code = parser.expr(function).compile()
	for i in range (lower_bound,upper_bound):
		for j in range (0,int(1/increments)):
			x=i+j*increments
			summation+=eval(code)*increments
	return summation
#successful Right HAND reimann sum.
def rightreimannsum(function, lower_bound, upper_bound, increments):
	summation=0
	code = parser.expr(function).compile()
	i=lower_bound
	for j in range (0,int((upper_bound-lower_bound)/increments)):
		x=i+j*increments
		summation+=eval(code)*increments
		
		
	return summation
print(rightreimannsum('1/(1+(x+tan(x))**2)', 0,1000, .001))

def trapazoidalreimannsum(function, lower_bound, upper_bound, increments):
	summation = (leftreimannsum(function, lower_bound, upper_bound, increments) + rightreimannsum(function, lower_bound, upper_bound, increments))*.5
	return summation
#successful double integral calculator if you use small increments
def doubleintegral(function, lower_x,upper_x, lower_y, upper_y, increments):
	summation=0
	code = parser.expr(function).compile()
	for l in range (0,int((upper_x-lower_x)/increments)):
		x=lower_x+l*increments
		for k in range (0,int((upper_y-lower_y)/increments)):
			y=upper_y-k*increments
			summation+=eval(code)*(increments**2)
	return summation

def tripleintegral(function,lower_x,upper_x, lower_y, upper_y, lower_z, upper_z, increments):
	summation=0
	code= parser.expr(function).compile()
	for l in range (0,int(1/increments)):
		x=lower_x+l*increments
		for k in range (0,int(1/increments)):
			y=lower_y+k*increments
			y=upper_y-y
			summation+=eval(code)*(increments**2)
	return summation

#successful triple integral calculator if you use small increments but takes longer time to run
def tripleintegral(function, lower_x,upper_x, lower_y, upper_y, lower_z, upper_z, increments):
	summation=0
	code = parser.expr(function).compile()
	for l in range (0,int((upper_x-lower_x)/increments)):
		x=upper_x-l*increments
		for k in range (0,int((upper_y-lower_y)/increments)):
			y=upper_y-k*increments
			for j in range(0,int((upper_z-lower_z)/increments)):
				z=upper_z-j*increments
				summation+=eval(code)*(increments**3)
	return summation

def derivativeatpoint(function, n):
	code = parser.expr(function).compile()
	x=n+.0001
	up=eval(code)
	x=n-.0001
	down=eval(code)
	derivative=(up-down)/.0002
	return derivative

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def secondderivativeatpoint(function,n):
	l=(derivativeatpoint(function, n+.0001) - derivativeatpoint(function, n-.0001))/.0002
	return l

