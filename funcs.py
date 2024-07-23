import pandas as pd
import numpy as np 
import yfinance as yf
import seaborn as sb
import funcs
from datetime import datetime 
import matplotlib.pyplot as plt



# function that calculates the bollinger bands. 
# 1. Calculate simple moving average 
# 2. calculate standard deviation 
# 3. Calculate bands add/substract (2*SD) to the SMA. 
# 4. Typically done in 20 day period intervals 

def calculate_bollinger_bands(stock_data, window=20, num_std_dev=2):
    stock_data['SMA'] = stock_data['Close'].rolling(window=window).mean()
    stock_data['STD'] = stock_data['Close'].rolling(window=window).std()
    stock_data['Upper Band'] = stock_data['SMA'] + (num_std_dev * stock_data['STD'])
    stock_data['Lower Band'] = stock_data['SMA'] - (num_std_dev * stock_data['STD'])
    return stock_data[['Close', 'SMA', 'Upper Band', 'Lower Band']]

def plot_bollinger_bands(stock, data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['SMA'], label='20 Period SMA', color='orange', linestyle='--')
    plt.plot(data['Upper Band'], label='Upper Band', color='green', linestyle='--')
    plt.plot(data['Lower Band'], label='Lower Band', color='red', linestyle='--')
    plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='gray', alpha=0.3)

    plt.title(f'Bollinger Bands for {stock}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    
    plt.show()