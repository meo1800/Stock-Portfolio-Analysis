from scripts.data_processing import weighted_cash_investment
import random
import pandas as pa
import numpy as np

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
    return_on_investment = (((weighted_portfolio_df['Portfolio Value [$]'][-1:])/
                            (weighted_portfolio_df['Portfolio Value [$]'][0])) - 1) * 100

    # Calculate Portfolio Daily Return
    portfolio_daily_return_df = weighted_portfolio_df.drop(columns = ['Portfolio Value [$]','Portfolio Daily Return [%]'])
    portfolio_daily_return_df = portfolio_daily_return_df.pct_change(1)

    expected_return = np.sum(weights * portfolio_daily_return_df.mean()) * 252 # Trading days in a year
    
    # Measures Portfolio Volatility (risk) using standard deviation.
    covariance = portfolio_daily_return_df.cov() * 252 
    expected_volatility = np.sqrt(np.dot(weights, np.dot(covariance, weights)))

    # Calcuate Sharpe ratio
    sharpe_ratio = (expected_return - RfR) / expected_volatility
   
    return expected_return, expected_volatility, sharpe_ratio, weighted_portfolio_df['Portfolio Value [$]'][-1:].values[0],return_on_investment.values[0]

# Print Simulation Engine Outcomes
def print_metrics(simulation_engine_return):
    print('Expected Portfolio Annual Return = {:.2f}%'.format(simulation_engine_return[0] * 100))
    print('Portfolio Standard Deviation (Volatility) = {:.2f}'.format(simulation_engine_return[1] * 100))
    print('Sharpe Ratio = {:.2f}'.format(simulation_engine_return[2] * 100))
    print('Portfolio Final Value = ${:.2f}'.format(simulation_engine_return[3]))
    print('Return on Investment = {:.2f}'.format(simulation_engine_return[4]))

