import pandas as pd
import numpy as np 
# import graph libraries 
# import yfinance as yf
from datetime import datetime 

# Start and end date times for bollinger bands calculations for the year 
end = datetime.now()
start = datetime(end.year-1, end.month, end.day)

# what stocks are we evaluating 
stock_list = []

# function that calculates the bollinger bands. 1. Calculate simple moving average 2. calculate standard deviation 3. Calculate bands add/substract (2*SD) to the SMA. 4. Typically done in 20 day period intervals 

def calculate_bollinger_bands(data, length = 20):
    data['SMA'] = data['Close'].rolling(length).mean()
    data['SD'] = data['Close'].rolling(length).std()
    #now calculating upper and lower bands 
    data['UB'] = data['SMA'] + (data['SD']*2)
    data['LB'] = data['SMA'] - (data['SD']*2)
    return data

#download stock data from yf and calculate bb
for stock in stock_list:
    globals()[stock] = yf.download(stock, start =start, end = end)
    globals()[stock] = calculate_bollinger_bands(globals()[stock])

# plot the function. Havent looked into this yet 





