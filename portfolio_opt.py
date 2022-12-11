import pypfopt
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

# Load the historical data for the stocks in your portfolio
data = pypfopt.tickers(["SPY", "AAPL", "GOOG", "IBM"])

# Calculate the expected returns and covariance matrix
mu = expected_returns.mean_historical_return(data)
S = risk_models.sample_cov(data)

# Optimize the portfolio using the Markowitz model
ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()
ef.portfolio_performance(verbose=True)
