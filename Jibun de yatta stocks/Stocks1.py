import alpha_vantage
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import math
key = 'TC5QY4ZPPJ2F29DB'

ts= TimeSeries(key = key,output_format='pandas', indexing_type = 'date') 
data,meta_data = ts.get_intraday('SPY', outputsize = 'full', interval = '5min')

print(data)

def smooth_data(data, n):
	data['smoothed'] = data['4. close']
	
	for i in range(n,len(data)-n):
		data['smoothed'][i]=0
		for j in range(n):
			data['smoothed'][i]+= (data['4. close'][i-n]+ data['4. close'][i+n])/(2*n)
		 
	
	return data


data = smooth_data(data,3)

target = 'smoothed'
out = int(math.ceil(.15*len(data)))
data['label'] = data[target].shift(-out)
data.fillna(-99999, inplace=True)
import numpy as np
from sklearn import preprocessing, svm
features = ['1. open', '5. volume']
X = np.array(data[features])
X_lately=X[:-out]
y= np.array(data['label'])
y_lately = y[:-out]
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_lately,y_lately,test_size = .8)

from sklearn.linear_model import LinearRegression

clf = LinearRegression()

clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)


import matplotlib.pyplot as plt
from matplotlib import style
a = []
for i in range(len(forecast_set)):
	a.append(i)

df = pd.DataFrame({'x':a, 'y':forecast_set})

style.use('ggplot')
plt.figure(0)
plt.title('Actual price for SPY stock (1 min)')
data[target].plot()


plt.figure(1)
plt.title('Predicted price for SPY stock (1 min)')
df.y.plot()





plt.show()