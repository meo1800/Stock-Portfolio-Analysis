from scripts.data_processing import weighted_cash_investment, get_financial_data
import random
import pandas as pa
import numpy as np
import streamlit as st

# Generates random portfolio weights for a given number of stocks, n 
def generate_portfolio_weights(n):
    weights = []
    for i in range(n):
        weights.append(random.random())
        
    # Ensures weights sum to one
    weights = weights/np.sum(weights)
    return weights


# Uses Portfolio Weights and Initial Investment Amount to find:
    # 1. Expected return
    # 2. Expected volatility
    # 3. Sharpe ratio
    # 4. ROI
    # 5. Final portfolio value

def simulation_engine(close_price_df,weights,initial_investment,RfR):
    # Uses weighted_cash_investment function to process 
    weighted_portfolio_df = weighted_cash_investment(close_price_df,weights,initial_investment)
    
    # Calculate ROI
    return_on_investment = (((weighted_portfolio_df['Portfolio Value [$]'].iloc[-1])/
                            (weighted_portfolio_df['Portfolio Value [$]'].iloc[0])) - 1) * 100

    # Calculate Portfolio Daily Return
    portfolio_daily_return_df = weighted_portfolio_df.drop(columns = ['Portfolio Value [$]','Portfolio Daily Return [%]'])
    portfolio_daily_return_df = portfolio_daily_return_df.pct_change(1)

    expected_return = np.sum(weights * portfolio_daily_return_df.mean()) * 252 # Trading days in a year
    
    # Measures Portfolio Volatility (risk) using standard deviation.
    covariance = portfolio_daily_return_df.cov() * 252 
    expected_volatility = np.sqrt(np.dot(weights, np.dot(covariance, weights)))

    # Calcuate Sharpe ratio
    sharpe_ratio = (expected_return - RfR) / expected_volatility
   
    return expected_return, expected_volatility, sharpe_ratio, weighted_portfolio_df['Portfolio Value [$]'][-1:].values[0],return_on_investment

# Print Simulation Engine Outcomes
def print_metrics(simulation_engine_return):
    print('Expected Portfolio Annual Return = {:.2f}%'.format(simulation_engine_return[0] * 100))
    print('Portfolio Standard Deviation (Volatility) = {:.2f}'.format(simulation_engine_return[1] * 100))
    print('Sharpe Ratio = {:.2f}'.format(simulation_engine_return[2]))
    print('Portfolio Final Value = ${:,.2f}'.format(simulation_engine_return[3]))
    print('Return on Investment = {:,.2f}%'.format(simulation_engine_return[4]))

def print_metrics_st(simulation_engine_return):
    st.write('Expected Portfolio Annual Return = {:.2f}%'.format(simulation_engine_return[0] * 100))
    st.write('Portfolio Standard Deviation (Volatility) = {:.2f}'.format(simulation_engine_return[1] * 100))
    st.write('Sharpe Ratio = {:.2f}'.format(simulation_engine_return[2]))
    st.write('Portfolio Final Value = ${:,.2f}'.format(simulation_engine_return[3]))
    st.write('Return on Investment = {:,.2f}%'.format(simulation_engine_return[4]))

def monte_carlo_simulation(stocks,start,end,RfR,initial_investment,runs):
   # Uses inputs to create a df using yfinance to obtain financial data
    portfolio_close_price_df = get_financial_data(stocks, start, end)

    # Defining input variables 
    # From user inputs
    sim_runs = runs
    n = len(stocks)

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
        expected_portfolio_returns_runs[i],volatility_runs[i],sharpe_ratio_runs[i],final_value_runs[i],return_on_investment_runs[i] = simulation_engine(portfolio_close_price_df,weights,initial_investment,RfR)

    # Finds the index and weights of the portfolio with the largest Sharpe ratio
    max_sharpe_index = np.argmax(sharpe_ratio_runs)
    weights_max_sharpe = weights_runs[max_sharpe_index, :]

    optimal_metrics = optimal_portfolio_return, optimal_volatility, optimal_sharpe_ratio, highest_final_value, optimal_return_on_investment = simulation_engine(portfolio_close_price_df,weights_max_sharpe,initial_investment,RfR)

    return st.write('Portfolio weights corresponding to the max Sharpe ratio:', ', '.join([f"{w:.4f}" for w in weights_max_sharpe])),print_metrics_st(optimal_metrics)
