import pypfopt
from pypfopt import risk_models
from pypfopt import expected_returns

# Load the historical data for the stocks in your portfolio
data = pypfopt.tickers(["SPY", "AAPL", "GOOG", "IBM"])

# Calculate the expected returns and covariance matrix
mu = expected_returns.mean_historical_return(data)
S = risk_models.sample_cov(data)

# Create the risk parity portfolio
rp = risk_models.RiskParityPortfolio(mu, S)

# Print the portfolio weights and performance metrics
print(rp.weights)
print(rp.portfolio_performance(verbose=True))
