#fantastic sorting algorithm
class ss(object):
	def superSort(int_arr):
		arr = []
		#...
		return arr
	#we now want to use this sorting method for strings even though currently only works on ints
	#goal is to be able to sort anything (objects included)
	object_array = []
	#casting each type of thing to an object and then putting it in the array we can make this more generic
	#casting to object means that we cant access the methods/variables in a lower levls object>person>student>undergrad
	#object equals method checks the memory location, so we need to override that

	#we also need to override the toString method to get useful information when we print the object __str__ method
# this code wont compile since these classes don't exist
arr = []
s = Student()
m = Monkey()
d = 'Hello world'
arr=[s,m,d]
#parameterized types
#create a container (idk python for containers) MyContainer<Monkey> = new MyContainer<Monkey>();
# MyContainer<Undergraduate> = new MyContainer<Undergraduate>();

# byte, short, int, long, double, char boolean are primative types 
# don't inherit from object
# Wrapper classes exist however which are objects Byte, Short, Long, Double, Integer, Char, Boolean
# Autoboxing - automatically trying to convert between them done in Java