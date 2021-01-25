import numpy as np
import parser
import math
from math import sin
from math import cos

import matplotlib.pyplot as plt 
  

def plotfunction(function1, function2, lower_x, upper_x):
	code = parser.expr(function1).compile()
	x=[]
	y=[]
	i=lower_x
	while i < upper_x:
		z=i
		i+=.001
		x.append(z)
		y.append(eval(code))
	plt.plot(x, y, label = "line 1" , color="green") 
	code = parser.expr(function2).compile()
	x=[]
	y=[]
	i=lower_x
	while i < upper_x:
		z=i
		i+=.001
		x.append(z)
		y.append(eval(code))
	plt.plot(x, y, label = "line 2", color = "blue") 
	plt.legend()
	plt.xlabel("x-axis")
	plt.ylabel("y-axis")
	plt.title("experiment", color= "purple")
	plt.ylim(0,1000)
	plt.xlim(0,15)
	plt.show() 
# example running plotfunction("z**2", 'z**3', 0,10)


def bargraph(left, height, labels, title):

	plt.bar(left, height, tick_label = labels, width = 0.8, color = ['red', 'green', 'black', 'blue']) 
	plt.xlabel('x - axis') 
	plt.ylabel('y - axis') 
	plt.title(title) 
	plt.show() 

# example running bargraph([1,2,3,4,5], [5,10,15,20,25], ['truck', 'car', 'isekai', 'murder', 'self-isekai'], 'Deaths in America (in millions)' )

def histogram(frequencies, lower_x, upper_x, bins ):
	range = (lower_x, upper_x)   
	plt.hist(frequencies, bins, range, color = 'green', 
        histtype = 'bar', rwidth = 0.8) 
	plt.xlabel('age') 
	plt.ylabel('No. of people') 
	plt.title('My histogram') 
	plt.show() 

# example running histogram([1,2,3,4,5,6,7,87,3,13,12,54,25,34,5634,62567,247,23,414,1424,56,], 0,10000, 2)

def scatterplot(x_values, y_values):
	plt.scatter(x_values, y_values, label= "whatever", color= "black", marker = "o", s=30)
	plt.xlabel('x-axis')
	plt.ylabel('y-axis')
	plt.title('whatever pt 2')
	plt.legend()
	plt.show()

# example running scatterplot([1,2,3,4,5,6,7,8,9,10], [30,20,15,24,0,3,5,30,44,40])

def piechart(sections, parts, colors):
	plt.pie(parts, labels = sections, colors = colors, startangle = 0, shadow= False, radius = 1, autopct = '%1.0f%%')
	plt.legend()
	plt.show()

# example running piechart(['games', 'anime', 'sleep', 'exercise'], [1,4,9,2], ['r', 'g', 'b', 'y'])

