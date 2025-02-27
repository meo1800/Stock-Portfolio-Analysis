from scripts.data_processing import get_financial_data,pct_daily_return,price_scalling

# Get user inputs for stock tickers, date range, risk-free-rate, initial investment, and simulation runs.
input_stocks = input('Enter stock tickers separated by a comma (ex: AAPL,AMZN,TSLA):').split(',')
input_start = input('Enter the start date of the investment in the form "YYYY-MM-DD":')
input_end = input('Enter the end date for the investment in the form "YYYY-MM-DD:')

# Uses inputs to create a df using yfinance to obtain financial data
portfolio_close_price_df = get_financial_data(input_stocks,input_start,input_end)

# Scales stock prices to 1
scaled_portfolio_df = price_scalling(portfolio_close_price_df)

# print(scalled_portfolio_df)