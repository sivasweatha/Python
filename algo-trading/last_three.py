# Import yfinance
import yfinance as yf

# Fetch NSE price data, from last 3 one minute candles
data = yf.download('^NSEI', period='4m', interval='1m')

# Display the data
print(data)