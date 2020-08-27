# Stock market dashboard about several stocks
import streamlit as st
import pandas as pd
from PIL import Image
st.write("""
# Stock Market Web Application
**Visually** show data on a stock! Date range from Jan 9, 2020 - July 31, 2020
""")

image = Image.open("/Users/lauralara/PycharmProjects/pythonProject1/stockimage.jpg")
st.image(image, use_column_width=True)

st.sidebar.header('User Input')

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-09")
    end_date = st.sidebar.text_input("End Date", "2020-07-31")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

def get_company(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'AAPL':
        return 'Apple'
    elif symbol == 'FB':
        return 'FaceBook'
    elif symbol == 'GOOG':
        return 'Alphabet'
    elif symbol == 'TSLA':
        return 'Tesla'
    else:
        'None'

def get_date(symbol, start, end):

    if symbol.upper() == 'AMZN':
        df = pd.read_csv("/Users/lauralara/PycharmProjects/pythonProject1/Stocks/AMZN.csv")
    elif symbol.upper() == 'AAPL':
        df = pd.read_csv("/Users/lauralara/PycharmProjects/pythonProject1/Stocks/AAPL.csv")
    elif symbol.upper() == 'FB':
        df = pd.read_csv("/Users/lauralara/PycharmProjects/pythonProject1/Stocks/FB.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("/Users/lauralara/PycharmProjects/pythonProject1/Stocks/GOOG.csv")
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("/Users/lauralara/PycharmProjects/pythonProject1/Stocks/TSLA.csv")
    else:
        df = pd.DataFrame(columns= ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row = 0
    end_row = 0

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i] ):
            start_row = i
            break

    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 -j
            break

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row +1, :]

start, end, symbol = get_input()
df = get_date(symbol, start, end)
company_name = get_company(symbol.upper())

st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

st.header(' Data Statistics')
st.write(df.describe())

