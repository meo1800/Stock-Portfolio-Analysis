from scripts.data_processing import get_financial_data,pct_daily_return,price_scalling
from scripts.analysis import generate_portfolio_weights,simulation_engine,print_metrics
# from scripts.visualizations import plot_financial_data
import numpy as np
import pandas as pd

# Get user inputs for stock tickers, date range, risk-free-rate, initial investment, and simulation runs.
# input_stocks = input('Enter stock tickers separated by a comma (ex: AAPL,AMZN,TSLA):').split(',')
# input_start = input('Enter the start date of the investment in the form "YYYY-MM-DD":')
# input_end = input('Enter the end date for the investment in the form "YYYY-MM-DD:')
# input_RfR = float.input('Enter the Risk-Free Rate (as a decimal):')
# input_initial_investment = float.input('Enter the initial investment amount ($):')
# input_runs = int.input('Enter the desired number of simulation runs:')

# input_stocks = ['AAPL','TSLA','MSTR','NVDA']
# input_start = "2020-03-01"
# input_end = "2025-03-01"
# input_RfR = 0.03
# input_initial_investment = 1000000
# input_runs = 10


def main_py(stocks,start,end,RfR,initial_investment,runs):
    # Uses inputs to create a df using yfinance to obtain financial data
    portfolio_close_price_df = get_financial_data(input_stocks,input_start,input_end)

    # Scales stock prices to 1
    scaled_portfolio_df = price_scalling(portfolio_close_price_df)

    # Calculates Daily Return of each stock
    portfolio_daily_returns_df = pct_daily_return(portfolio_close_price_df)

    # # Returns asset allocation according to a given weight and initial investment
    # asset_allocation = weighted_cash_investment(portfolio_close_price_df,)

    # # Plots a line chart of all stock prices
    # fig_pct_daily_return = plot_financial_data(portfolio_close_price_df,'Portfolio Positions [$]')

    # MONTE CARLO Simulation

    # Defining input variables 
    # From user inputs
    sim_runs = input_runs
    initial_investment = input_initial_investment
    n = len(input_stocks)

    # Placeholders to store values
    weights_runs = np.zeros((sim_runs, n))
    sharpe_ratio_runs = np.zeros(sim_runs)
    expected_portfolio_returns_runs = np.zeros(sim_runs)
    volatility_runs = np.zeros(sim_runs)
    return_on_investment_runs = np.zeros(sim_runs)
    final_value_runs = np.zeros(sim_runs)

    for i in range(sim_runs):
        # Generate random weights
        weights = generate_portfolio_weights(n)
        # Store weights in predefined matrix
        weights_runs[i,:] = weights

        # Using simulation_engine function 
        metrics = expected_portfolio_returns_runs[i],volatility_runs[i],sharpe_ratio_runs[i],final_value_runs[i],return_on_investment_runs[i] = simulation_engine(portfolio_close_price_df,weights,input_initial_investment,input_RfR)
    return metrics    
    

    # # print weights and portoflio metrics with each run 
    # print("Weights = {}".format(weights_runs[i].round(3)))
    # print_metrics(metrics)
    # # print("Simulation Run = {}".format(i))
    # # print("Weights = {}".format(weights_runs[i].round(3)))
    # # print("Final Value = ${:.2f}".format(final_value_runs[i]))
    # # print("Sharpe ratio = {:.2f}".format(sharpe_ratio_runs[i]))
    # print("\n")

