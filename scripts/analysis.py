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

