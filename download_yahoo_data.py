import yfinance as yf
import os
import pandas as pd


folder_path = 'yahoo'
os.makedirs(folder_path, exist_ok=True)

ticker_symbols = {
    # Commodities
    'WTI_Crude_Oil': 'CL=F',
    'Brent_Crude_Oil': 'BZ=F',
    'Natural_Gas': 'NG=F',
    'Silver': 'SI=F',
    'Gold': 'GC=F',
    'Copper': 'HG=F',
    'Corn': 'CORN',
    'Soybeans': 'SOYB',
    'Wheat': 'WEAT',
    'Coffee': 'KC=F',
    'Sugar': 'SB=F',

    # Cryptocurrencies
    'BTC': 'BTC-USD',
    'ETH': 'ETH-USD',
    'LTC': 'LTC-USD',
    'XRP': 'XRP-USD',
    'ADA': 'ADA-USD',
    'SOL': 'SOL-USD',
    'DOT': 'DOT-USD',
    'MATIC': 'MATIC-USD',

    # Stock Indices
    'S&P500': 'SPY',  # S&P 500 ETF
    'NASDAQ_COMPOSITE': '^IXIC',
    'RUSSELL2000': '^RUT',

    # Diverse Stocks from Different Sectors
    'AAPL': 'AAPL',   # Technology
    'AMZN': 'AMZN',   # Consumer Discretionary
    'GOOGL': 'GOOGL', # Communication Services
    'FB': 'META',     # Communication Services (Meta Platforms)
    'MSFT': 'MSFT',   # Technology
    'NFLX': 'NFLX',   # Communication Services
    'JNJ': 'JNJ',     # Healthcare
    'PFE': 'PFE',     # Healthcare (Pfizer)
    'XOM': 'XOM',     # Energy
    'WMT': 'WMT',     # Consumer Staples
    'TSLA': 'TSLA',   # Automotive
    'BA': 'BA',       # Industrials
    'VZ': 'VZ',       # Telecommunications
    'DIS': 'DIS',     # Entertainment
    'NKE': 'NKE',     # Consumer Discretionary (Nike)
    'PEP': 'PEP',     # Beverages (PepsiCo)
    'T': 'T',         # Telecommunications (AT&T)
    'HD': 'HD',       # Consumer Discretionary (Home Depot)
}

# Define the start and end dates for the data
start_date = '2000-01-01'
end_date = '2024-10-31'

# Download and save the data for each ticker symbol
for asset, ticker_symbol in ticker_symbols.items():
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
    data = data.resample('M').last()
    file_name = f"{folder_path}/{asset}.csv"
    data.to_csv(file_name)
    print(f"{asset.capitalize()} data saved to '{file_name}'")