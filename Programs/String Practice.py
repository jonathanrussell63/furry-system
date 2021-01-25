import random
def count(lists, word):
	c=0
	for i in range(len(lists)):
		if lists[i]== word:
			c+=1
	return c

def isin(list, word):
	truth=False
	for i in range(len(list)):
		if list[i]==word:
			truth=True
	return truth

def reverse(lists):
	newone=[]
	for i in range (len(lists)):
		newone.append(lists[len(lists)-1-i])
	return newone

def index(lists, word):
	found=False
	position=-1
	for i in range(len(lists)):
		if found==False:
			if lists[i]==word:
				position=i
	return position

def insert(lists, thing, position):
	a=lists[0:position]
	b=lists[position:]
	c=[thing]
	return a+c+b

def randasdasdoms(lists):
	newlist=[]
	for i in range(len(lists)):
		a= int(random.random()*len(lists))
		newlist.append(lists.pop(a))
	return newlist	

	