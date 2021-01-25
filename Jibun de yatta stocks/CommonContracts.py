import numpy as np
import math

#the formulas from the book correspond decently, only issue is of course with the change in volatility over time``

class Call():
	def __init__(self, S, D, T, E, r, v, t):
		self.S = S
		self.D = D
		self.T = T
		self.E = E
		self.r = r
		self.v = v
		self.t = t


	def value(self):
		d1 = math.log(self.S/self.E) + (self.r-self.D+.5*self.v**2)*(self.T-self.t)
		d2 = d1-self.v*((self.T-self.t)**.5)

		n1 = 0
		n2 = 0 
		for i in range(-10000, int(d1/.001)):
				x = i*.001
				n1 += 1/(2*math.pi)**.5 * math.exp(-.5*(x**2))*.001

		for i in range(-10000, int(d2/.001)):
				x = i*.001
				n2 += 1/(2*math.pi)**.5 * math.exp(-.5*(x**2))*.001

		v = self.S*math.exp(-self.D* (self.T-self.t))*n1-self.E*math.exp(-self.r*(self.T-self.t))*n2

		return v


	def delta(self):
		d1 = math.log(self.S/self.E) + (self.r-self.D+.5*self.v**2)*(self.T-self.t)		
		n1 = 0
		for i in range(-10000, int(d1/.001)):
				x = i*.001
				n1 += 1/(2*math.pi)**.5 * math.exp(-.5*(x**2))*.001

		delt = math.exp(-self.D*(self.T-self.t))*n1

		return delt 

	#def gamma (self):



# i think that this only works using the short term IV and not long term IV. Tends to overprice otherwise
a = Call(336.6,0,13/12,335,.08,.2064,0)

print(a.value())
print(a.delta())





#class Put():


#class BinaryCall():


#class BinaryPut():