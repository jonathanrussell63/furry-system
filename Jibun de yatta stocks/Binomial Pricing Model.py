# starting price S
# time step = 1/252
# r= itnerest rate
# standard deviation = std
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as si

#calculates all possible values of the stocks value based on binmial expansion
def stockValues(t_step, S, r, deviation, T):
	u = 1+deviation*(t_step)**.5
	v = 1-deviation*(t_step)**.5
	prices = []
	n_steps= T/t_step
	count = n_steps
	while count>0:
		for i in range(int(n_steps),-1,-1):
			prices.append(S*(u**i)*(v**(n_steps-i)))
			if i>0:
				count -=1

	option_values = [prices[x]-S for x in range(len(prices))]
	for i in range(len(option_values)):
		if option_values[i]<=0:
			option_values[i]=0

	optionPrices(option_values, n_steps, r, t_step, deviation)

#will be used to print out the option values for each layer of times, the first value of the option at the end
def optionPrices(option_values, n_steps, r, t_step,deviation):
	p = .5+r/(2*deviation)*(t_step)**.5
	layer_1_back = [option_values]
	count = 1
	while count <= n_steps+1:
		layer_1_back.append([])
		for i in range(len(layer_1_back[count-1])-1):
			layer_1_back[count].append(math.exp(-r*t_step)*(p*(layer_1_back[count-1][i])+(1-p)*layer_1_back[count-1][i+1]))
		count +=1
	a= layer_1_back
	a.pop(-1)
	for line in a:
		print (line)

#stocks = stockValues(1/1000, 1646.31,.1,.6413, 18/1000)
#using smaller time_steps makes it converge to actual price faiirly decently
# this method is *slightly* off on american methods since you are allowed to pull out early, it actually overprices them


def SimulateBrownianStock(price, drift, time_step, volatility):
	S0 = price
	prices = [price]
	t = [0]
	for i in range(52):
		S0 = S0*(1+drift*time_step+volatility*np.random.normal(0,1)*(time_step)**.5)
		prices.append(S0)
		t.append(i*time_step)
	plt.xlabel('WEEK')
	plt.ylabel('PRICE')
	plt.legend('Stock Price')
	plt.plot(t,prices)
	plt.show()
	prices = np.array(prices)
	mean = np.mean(prices)
	std = np.std(prices)
	returns = pd.DataFrame(prices).pct_change()




	print("Returns Mean: ",np.mean(returns[0][1:]), "Returns STD: ", np.std(returns[0][1:]))




SimulateBrownianStock(168,.1/52,1,0.25)

