import parser
import math
from math import sin
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
	for i in range (lower_bound,upper_bound):
		for j in range (0,int(1/increments)):
			x=i+j*increments
			x=upper_bound-x
			summation+=eval(code)*increments
	return summation

def trapazoidalreimannsum(function, lower_bound, upper_bound, increments):
	summation = (leftreimannsum(function, lower_bound, upper_bound, increments) + rightreimannsum(function, lower_bound, upper_bound, increments))*.5
	return summation


print(trapazoidalreimannsum("x**4",0,10,.0001))
