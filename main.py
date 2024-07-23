import pandas as pd
import numpy as np 
import yfinance as yf
import seaborn as sb
import funcs
from datetime import datetime 
import matplotlib.pyplot as plt

# Start and end date times for bollinger bands calculations for the year 
end = datetime.now()
start = datetime(end.year-1, end.month, end.day)

# what stocks are we evaluating 
stock_list = ["MSFT"]


#yf Ticker contains these keys, stored as a hashmap
#['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 
# 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 
# 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 
# 'yearChange', 'yearHigh', 'yearLow']




#hashmap, stock name as key, its yfinance object as value
#takes list of stocks and turns it into data
ticker_list = {}
for stock in stock_list:
    ticker_list[stock] = yf.download(stock, start = start, end = end)
    

#hashmap, stock name as key, its bollinger bands as its value
#takes list of stock data and turns it into bollinger bands
bollinger_list = {}
for stock in ticker_list:
    stock_data = ticker_list[stock]
    bollinger_list[stock] = funcs.calculate_bollinger_bands(stock_data)


# Plots the bollinger bands in bollinger_list
for stock in bollinger_list:
    bollinger_data = bollinger_list[stock]
    funcs.plot_bollinger_bands(stock, bollinger_data)



#To do @preddy
#Potentially store stock as a dataframe instead of having many hashamps
#current using hashmap with stock name as key(string), and various values
#could potentially use a dataframe with stock name (string) and primary key
#append to dataframe a collumn for bollinger bands, then to plot them call function on that collumn


