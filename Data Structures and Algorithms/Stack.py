# stack data structure
# Stack main idea
# Books : A,B,C,D are laying on the floor and we want to stack them up neatly
# A,     B,C,D
# A,B    C,D
# A,B,C  D
# A,B,C,D
# To retrieve an element we can only access the top book (D)
# To access the A book we have to take off D,C,B first

# putting something on the stack = pushing, replaces top element with that book
# popping = taking off the top element and putting it down
# view = retrieve info of top element

#implementation
class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)
	
	#returns the top element on the stack
	def pop(self):
		return self.items.pop()

	def get_stack(self):
		return self.items

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else :
			return self.items

# Problem: determine if a set of parenthesis are balanced or not via a stack
# Balanced : (), ()(), (({[]}))
# Not-balanced : ((), {{(])}}, [][]]]

#loop through string adding left sided parentheses to stack, when encounter a right parenthesis pop top element off stack and check if it matches


def is_balanced(string):
	s= Stack()
	if len(string)%2!=0:
		return False

	bal = True
	for i in string:

		if i == '(' or i == '[' or i == '{':
			s.push(i)
		else:
			if s.is_empty():
				return False
			elif  (i==')' and s.pop()!='(') or (i==']' and s.pop()!='[') or (i=='}' and s.pop()!='{'):
				return False

	return True


	

#convert from integer to binary representations via a stack
# ex 242,
# 242/2 = 121 r 0
# 121/2 = 60 r 1
# ...
# reading remainders backwards gives binary representation

def binary(num):
	f = Stack()
	if num<2:
		return num%2
	else:
		while num>0:
			remainder = num%2
			num = num//2
			f.push(remainder)
		binary = ''
		while not f.is_empty():
			binary += str(f.pop())
		return binary

def reverse_string(string):
	rev = ''
	s = Stack()
	for i in string:
		s.push(i)

	while not s.is_empty():
		rev += s.pop()
	return rev

print(reverse_string('hello'))