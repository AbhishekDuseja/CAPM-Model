# plot_capm.py

import matplotlib.pyplot as plt
import numpy as np

from capm import get_data, calculate_returns, calculate_capm

def plot_capm_line(stock_returns, index_returns, beta, expected_return):
    plt.figure(figsize=(10, 6))
    plt.scatter(index_returns, stock_returns, alpha=0.6, label='Data points')
    
    x = np.linspace(index_returns.min(), index_returns.max(), 100)
    y = beta * x + expected_return
    plt.plot(x, y, color='red', label='CAPM Line')
    
    plt.title('CAPM Model')
    plt.xlabel('Market Index Returns')
    plt.ylabel('Stock Returns')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    stock_ticker = 'AAPL'  # Replace with actual stock ticker
    index_ticker = 'SPY'   # Replace with actual index ticker
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    
    stock_prices, index_prices = get_data(stock_ticker, index_ticker, start_date, end_date)
    
    stock_returns = calculate_returns(stock_prices)
    index_returns = calculate_returns(index_prices)
    
    beta, expected_return = calculate_capm(stock_returns, index_returns)
    
    plot_capm_line(stock_returns, index_returns, beta, expected_return)

if __name__ == "__main__":
    main()
