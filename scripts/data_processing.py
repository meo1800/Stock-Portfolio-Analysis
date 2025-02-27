import yfinance as yf
import pandas as pd 
import numpy as np

# Function to get financial data of portfolio from inputs using yfinance
def get_portfolio_data(list, start, end):
    df = yf.download(list, start = start, end = end)['Close']
    return df

portfolio_close_price = get_portfolio_data(input_stocks,input_start,input_end)

# Calculate the percentage daily return of each stock, including all rows and skipping the data column
stock_daily_returns = portfolio_close_price.iloc[:,1:].pct_change() * 100

# Replacing NaN with zero in the first row
stock_daily_returns.replace(np.nan,0,inplace = True)

# Function to scale stock prices to 1
def price_scalling(raw_prices_df):
    scaled_prices_df = raw_prices_df.copy()
    for i in scaled_prices_df.columns[:]:
        scaled_prices_df[i] = raw_prices_df[i]/raw_prices_df[i].iloc[0]
    return scaled_prices_df

scalled_portfolio = price_scalling(portfolio_close_price)








