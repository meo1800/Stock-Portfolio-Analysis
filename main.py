from scripts.data_processing import get_financial_data,pct_daily_return,price_scalling,weighted_cash_investment
from scripts.visualizations import plot_financial_data
import streamlit as st

# Get user inputs for stock tickers, date range, risk-free-rate, initial investment, and simulation runs.
input_stocks = input('Enter stock tickers separated by a comma (ex: AAPL,AMZN,TSLA):').split(',')
input_start = input('Enter the start date of the investment in the form "YYYY-MM-DD":')
input_end = input('Enter the end date for the investment in the form "YYYY-MM-DD:')
input_RfR = input('Enter the Risk-Free Rate (as a decimal):')
input_initial_investment = input('Enter the initial investment amount ($):')
input_runs = input('Enter the desired number of simulation runs:')

# Uses inputs to create a df using yfinance to obtain financial data
portfolio_close_price_df = get_financial_data(input_stocks,input_start,input_end)

# Scales stock prices to 1
scaled_portfolio_df = price_scalling(portfolio_close_price_df)

# Calculates Daily Return of each stock
portfolio_daily_returns_df = pct_daily_return(portfolio_close_price_df)


asset_allocation = weighted_cash_investment(portfolio_close_price_df)

# Plots a line chart of all stock prices
fig_pct_daily_return = plot_financial_data(portfolio_close_price_df,'Portfolio Positions [$]')
