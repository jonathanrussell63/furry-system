import pandas as pd
from pandas import read_csv
import math

	
data = open('MSFT.csv')
data = pd.read_csv(data)

#using the Rogers and Satchell Drift Dependant method to calculate volatility
def calc_vol(data):
	vol_2 = 0
	for i in range(len(data)):
		vol_2 += math.log(data['High'][i]/data['Close'][i])*math.log(data['High'][i]/data['Open'][i])+math.log(data['Low'][i]/data['Close'][i])*math.log(data['Low'][i]/data['Open'][i])
	vol_2/=len(data)
	return((vol_2**.5)*(365**.5))
print(calc_vol(data))
#numerical way to calculate implied volatility
import numpy as np
from scipy.stats import norm
N = norm.cdf

def bs_call(S, K, T, r, vol):
    d1 = (np.log(S/K) + (r + 0.5*vol**2)*T) / (vol*np.sqrt(T))
    d2 = d1 - vol * np.sqrt(T)
    return S * norm.cdf(d1) - np.exp(-r * T) * K * norm.cdf(d2)

def bs_vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)

def find_vol(target_value, S, K, T, r, *args):
    MAX_ITERATIONS = 200
    PRECISION = 1.0e-2
    sigma = 0.5
    for i in range(0, MAX_ITERATIONS):
        price = bs_call(S, K, T, r, sigma)
        vega = bs_vega(S, K, T, r, sigma)
        diff = target_value - price  # our root
        if (abs(diff) < PRECISION):
            return sigma
        
        sigma = sigma + diff/vega # f(x) / f'(x)
    return sigma # value wasn't found, return best guess so far
	
#A stock is at 100, a call has strike 100, expiration in one year, interest rate 5%
#and the option market price is $10.45. What volatility are traders using?
#print(find_vol( 10.45,100, 100,1,.05)) #=.2