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

def simulation_engine(close_price_df,weights,initial_investment):
    # Uses weighted_cash_investment function to process 
    weighted_portfolio_df = weighted_cash_investment(close_price_df,weights,initial_investment)
    
    # Calculate ROI
    return_on_investment = (((weighted_portfolio_df['Portfolio Value [$]'][-1:])/
                            (weighted_portfolio_df['Portfolio Value [$]'][0])) - 1) * 100

    #Calculate Portfolio Daily Return
    portfolio_daily_return_df = weighted_portfolio_df.drop(columns = ['Portfolio Value [$]','Porfolio Daily Return [%]'])
    portfolio_daily_return_df = portfolio_daily_return_df.pct_change(1)

    expected_return = np.sum(weights * portfolio_daily_return_df)   
    g