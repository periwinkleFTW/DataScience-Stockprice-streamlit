import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

# Ticker
ticker_symbol = 'GOOGL'

# Get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# Get historial prices for this ticker
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing price
""")
st.line_chart(ticker_df.Close)

st.write("""
## Volume
""")
st.line_chart(ticker_df.Volume)