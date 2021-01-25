import math
from math import sin
from math import cos
import parser
"""function = str(input("Give me a function "))
lower= int(input("Give me a lower bound "))
upper = int(input("Give me an upper bound "))
maximum=0
value_of_x=0
for i in range (0,100000):
	x=lower+(upper-lower)*i/100000
	code = parser.expr(function).compile()
	f=eval(code)
	if(f>maximum):
		maximum=f
		value_of_x=x

print("The maximum on the interval is "+ str(maximum))
print("The value of x it occurs is at x="+str(value_of_x))
"""
zero=[]
def derivativezero(function, lower, upper):
	lower=-5
	upper=5
	function="x**2"
	
	code = parser.expr(function).compile()
	for i in range(0,20000):
		x1=lower+(upper-lower)*i/20000
		x2=lower+(upper-lower)*(i+1)/20000
		x=x1
		f1=eval(code)
		x=x2
		f2=eval(code)
		derivative=(f2-f1)*10000/(upper-lower)
		if(derivative < .001 and derivative>-.001):
			zero.append(x1)

def eliminatesimilar(zeros):
	elements=zeros
	for i in range(0,len(elements)):
		for j in range(i,len(elements)):
			if((elements[i]-elements[j])<.05 and (elements[i]-elements[j])>-.05):
				elements.remove(elements[j])
	return elements
derivativezero("x^2",-5,5)
print(zero)
print(eliminatesimilar(zero))

