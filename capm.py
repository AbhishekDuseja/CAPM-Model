# capm.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def get_data(stock_ticker, index_ticker, start_date, end_date):
    # Here you would retrieve historical price data using a financial data API or a CSV file
    # For simplicity, let's assume you have a function to fetch data
    
    # Example:
    # stock_prices = fetch_prices(stock_ticker, start_date, end_date)
    # index_prices = fetch_prices(index_ticker, start_date, end_date)
    
    # For demonstration, we generate some random data
    np.random.seed(0)
    dates = pd.date_range(start=start_date, end=end_date)
    stock_prices = pd.Series(np.random.randn(len(dates)), index=dates)
    index_prices = pd.Series(np.random.randn(len(dates)), index=dates)
    
    return stock_prices, index_prices

def calculate_returns(prices):
    return prices.pct_change().dropna()

def calculate_capm(stock_returns, index_returns):
    beta, alpha, r_value, p_value, std_err = stats.linregress(index_returns, stock_returns)
    expected_return = alpha + beta * index_returns.mean()
    return beta, expected_return

def main():
    # Example usage
    stock_ticker = 'AAPL'  # Replace with actual stock ticker
    index_ticker = 'SPY'   # Replace with actual index ticker
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    
    stock_prices, index_prices = get_data(stock_ticker, index_ticker, start_date, end_date)
    
    stock_returns = calculate_returns(stock_prices)
    index_returns = calculate_returns(index_prices)
    
    beta, expected_return = calculate_capm(stock_returns, index_returns)
    
    print(f"Beta: {beta}")
    print(f"Expected return: {expected_return}")

if __name__ == "__main__":
    main()
