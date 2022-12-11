import pyalgotrade

# Load the historical data for the stock you want to test
data = pyalgotrade.feeds.YahooFeed("SPY")

# Create the SMA strategy
sma = pyalgotrade.strategy.SMAStrategy(data, 50, 200)

# Run the strategy
sma.run()

# Print the results
print(sma.getResult())
