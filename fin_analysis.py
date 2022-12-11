import pandas as pd
import matplotlib.pyplot as plt

# Import the data into a pandas DataFrame
df = pd.read_csv('company_earnings.csv')

# Calculate the company's earnings per share (EPS)
eps = df['net_income'] / df['shares_outstanding']

# Add the EPS data to the DataFrame
df['eps'] = eps

# Plot the EPS data over time
plt.plot(df['date'], df['eps'])
plt.xlabel('Date')
plt.ylabel('Earnings per Share')
plt.show()
