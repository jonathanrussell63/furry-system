#creates a class called coordinate with the parent class of object

class Coordinate(object):
	# need attributes/methods here
	#special method called __inti__
	def __init__(self, x,y):
		self.x=x
		self.y=y

	def distance(self, other):
		x_diff_sq = (self.x-other.x)**2
		y_diff_sq = (self.y-other.y)**2
		return (x_diff_sq+y_diff_sq)**.5

	def __str__(self):
		return '<'+str(self.x)+','+str(self.y)+'>'

class Animal(object):
	# using getter and setter methods
	def __init__(self, age):
		self.age = age
		self.name = None
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	def set_age(self, newage):
		self.age = newage
	def set_name(self, newname=""):
		self.name = newname
	def __str__(self):
		return "animal:"+str(self.name)+":"+str(self.age)
	def __eq__(self, obj1):
		if (self.get_name() == obj1.get_name()) and (self.get_age() == obj1.get_age()):
			return True
		else: 
			return False

#sub-class / inheritance of animal class
class Cat(Animal):
	def speak(self):
		prnit('meow')

	def __str__(self):
		return "cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal):
	tag=1
	def __init__(self, age, parent1=None, parent2=None):
		Animal.__init__(self,age)
		self.parent1= parent1
		self.parent2= parent2
		self.rid = Rabbit.tag
		Rabbit.tag+=1

	def get_rid (self):
		return str(self.rid).zfill(3)
	def get_parent1(self):
		return self.parent1
	def get_parent2(self):
		return self.parent2
	def __add__(self, other):
		return Rabbit(0, self, other)

a=Rabbit(5)
b = Rabbit(5)
c = a+b
print(a.__eq__(b))

