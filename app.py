import streamlit as st
from scripts.analysis import monte_carlo_simulationgit as

st.title("Hello, Streamlit!")

st.sidebar.header("User Input")

# Get user inputs for stock tickers, date range, risk-free-rate, initial investment, and simulation runs.
input_stocks = st.sidebar.text_input('Enter stock tickers separated by a comma:','AAPL,AMZN,TSLA').split(',')
input_start = st.sidebar.text_input('Enter the start date of the investment in the form "YYYY-MM-DD":','2020-03-03')
input_end = st.sidebar.text_input('Enter the end date for the investment in the form "YYYY-MM-DD:','2025-03-03')
input_RfR = st.sidebar.number_input('Enter the Risk-Free Rate (as a decimal):',0.03)
input_initial_investment = st.sidebar.number_input('Enter the initial investment amount [$]:',1000000)
input_runs = st.sidebar.slider('Enter the desired number of simulation runs:', min_value = 10,max_value = 10000, value = 5000)

# st.write({monte_carlo_simulation(input_stocks,input_start,input_end,input_RfR,input_initial_investment,input_runs)})

if st.sidebar.button("Run Monte Carlo Simulation"):
    with st.spinner("Running simulations... Please wait."):
        results = monte_carlo_simulation(input_stocks, input_start, input_end, input_RfR, input_initial_investment, input_runs)
    
    # Display results
    st.write("Simulation Results:")
    st.write(results)