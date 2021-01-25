import alpha_vantage
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
key = 'TC5QY4ZPPJ2F29DB'

ts= TimeSeries(key = key,output_format='pandas', indexing_type = 'date') #can also use indexing_type = 'integer', output_format = 'csv' json by default

data,meta_data = ts.get_intraday('MSFT', interval = '1min', outputsize = 'full')

#Plotting

import matplotlib.pyplot as plt
#data['4. close'].plot()
#plt.title('Intraday Times Series for the MSFT stock (1 min)')
#plt.show()

#Technical indicators
from alpha_vantage.techindicators import TechIndicators

#ti = TechIndicators (key =key, output_format ='pandas')
#data,meta_data = ti.get_bbands(symbol = 'MSFT', interval = '60min', time_period=60)
#data.plot()
#plt.title('BBands indicator for MSFT stock (60 min)')
#plt.show()

#Getting sector performances
from alpha_vantage.sectorperformance import SectorPerformances

#sp = SectorPerformances(key = key, output_format = 'pandas')
#data,meta_Data = sp.get_sector()
#data['Rank A: Real-Time Performance'].plot(kind ='bar')
#plt.title('Real Time Performance (%) per sector')
#plt.tight_layout()
#plt.grid()
#plt.show()

#Crypto currencies
from alpha_vantage.cryptocurrencies import CryptoCurrencies

#cc = CryptoCurrencies(key=key, output_format = 'pandas')
#data,meta_data = cc.get_digital_currency_daily(symbol ='BTC', market = 'CNY')
#data['4b. close (USD)'].plot()
#plt.tight_layout()
#plt.title('Daily close for BTC')
#plt.grid()
#plt.show()

#FOREX
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint

#cc = ForeignExchange(key='YOUR_API_KEY')
# There is no metadata in this call
#data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
#pprint(data)

#improves performance using multiple api calls:
import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries

#symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']


#async def get_data(symbol):
#    ts = TimeSeries(key='YOUR_KEY_HERE')
#    data, _ = await ts.get_quote_endpoint(symbol)
#    await ts.close()
#    return data

#loop = asyncio.get_event_loop()
#tasks = [get_data(symbol) for symbol in symbols]
#group1 = asyncio.gather(*tasks)
#results = loop.run_until_complete(group1)
#loop.close()
#print(results)

