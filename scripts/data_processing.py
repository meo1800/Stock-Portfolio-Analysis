import yfinance as yf
import pandas as pd 
import numpy as np

# Get financial data of portfolio from inputs using yfinance
def get_financial_data(list, start, end):
    df = yf.download(list, start = start, end = end)['Close']
    return df

# Calculate the percentage daily return of each stock, including all rows and columns
def pct_daily_return(df):
    daily_returns = df.iloc[:].pct_change() * 100
    daily_returns.replace(np.nan,0,inplace = True) # Replaces NaN in first row with zero
    return daily_returns

# Scales stock prices to 1
def price_scaling(raw_prices_df):
    scaled_prices = raw_prices_df.copy()
    for i in scaled_prices.columns[:]:
        scaled_prices[i] = raw_prices_df[i]/raw_prices_df[i].iloc[0]
    return scaled_prices

# Returns a df with the portfolio's weighted cash investment of each stock
# Adds columns for Total Portfolio Value and Daily Return
def weighted_cash_investment(raw_prices_df,weights,initial_amount):

    scaled_prices_df = price_scaling(raw_prices_df)
    weighted_portfolio_df = pd.DataFrame(index = scaled_prices_df.index)
    
    # Obtains stock names along with counter to be used as an index
    for i, stock in enumerate(scaled_prices_df.columns[1:]):
        weighted_portfolio_df[stock] = weights[i] * scaled_prices_df[stock]  * initial_amount
    
    # Add column (Total Portfolio Value)
    weighted_portfolio_df['Portfolio Value [$]'] = weighted_portfolio_df.sum(axis = 1, numeric_only = True)
    
    # Add column (Portfolio Daily Return) and replace NaNs with zero
    weighted_portfolio_df['Portfolio Daily Return [%]'] = weighted_portfolio_df['Portfolio Value [$]'].pct_change(1) * 100
    weighted_portfolio_df.replace(np.nan, 0, inplace = True)
    
    return weighted_portfolio_df.round(2)









