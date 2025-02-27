import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import cufflinks as cf

# Plots a line chart of stock prices
def plot_financial_data(df, title):
    
    fig = px.line(title = title)
    
    # For loop that plots all stock prices in the pandas dataframe df
    for i in df.columns[:]:
        fig.add_scatter(x = df['Date'], y = df[i], name = i)
        fig.update_traces(line_width = 1)
        fig.update_layout({'plot_bgcolor': "white"})

    fig.show()





# figure = cf.QuantFig(JPM_df, title = 'JPMorgan Chase Candlestick', name = 'JPM')
# figure.add_sma(periods= [30,100], column = 'Close', color = ['magenta', 'green'])
# figure.iplot(theme = 'white', up_color = 'green', down_color = 'red')

# figure = cf.QuantFig(JPM_df, title = 'JPMorgan Chase Candlestick', name = 'JPM')
# figure.add_bollinger_bands(periods = 20, boll_std= 2, color = ['yellow', 'blue'])
# figure.iplot()

# # Plot histograms for stocks daily returns using plotly express
# # Compare META to JNJ daily returns histograms
# fig = px.histogram(daily_returns_df.drop(columns = ['Date']))
# fig.update_layout({'plot_bgcolor': "white"})

# # Plot a heatmap showing the correlations between daily returns
# # Strong positive correlations between Catterpillar and John Deere - both into heavy equipment and machinery
# # META and Google - both into Tech and Cloud Computing
# plt.figure(figsize = (10, 8))
# sns.heatmap(daily_returns_df.drop(columns = ['Date']).corr(), annot = True);

# sns.pairplot(daily_returns_df);