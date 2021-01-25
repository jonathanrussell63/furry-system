d = {}
l=[]
d[1]= 'yes'
d['1'] = 'no'
class my_class:
	def init(self):
		self.data = 'data'

instance = my_class()
d['object'] = instance

for key in d.keys():
	print(d[key])