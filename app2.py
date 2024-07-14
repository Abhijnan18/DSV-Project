import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

# Function to get stock data


def get_stock_data(ticker, start_date, end_date):
    # Check if the ticker is for an Indian stock (ends with ".NS" for NSE or ".BO" for BSE)
    if ticker.endswith(".NS") or ticker.endswith(".BO"):
        ticker = ticker.replace(".NS", ".NS").replace(
            ".BO", ".BO")  # Ensure correct suffix
        stock_data = yf.download(ticker, start=start_date, end=end_date)
    else:
        st.error(
            "Currently, only Indian stocks ending with '.NS' or '.BO' are supported.")
        stock_data = None
    return stock_data

# Main Streamlit app


def main():
    st.title("Stock Market Analysis")

    # Sidebar for user input
    st.sidebar.header("Stock Selection")
    ticker = st.sidebar.text_input(
        "Enter stock ticker (e.g., TCS.NS)", "TCS.NS")
    start_date = st.sidebar.date_input(
        "Start date", pd.to_datetime("2024-06-07"))
    end_date = st.sidebar.date_input("End date", pd.to_datetime("today"))

    # Fetching the stock data
    stock_data = get_stock_data(ticker, start_date, end_date)

    if stock_data is not None:
        # Displaying the stock data
        st.subheader(f"{ticker} Stock Data")
        st.write(stock_data)

        # Line chart of closing prices
        st.subheader("Line Chart - Closing Prices")
        st.line_chart(stock_data['Close'])

        # Candlestick chart
        st.subheader("Candlestick Chart")
        fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                             open=stock_data['Open'],
                                             high=stock_data['High'],
                                             low=stock_data['Low'],
                                             close=stock_data['Close'])])
        st.plotly_chart(fig)

        # Compare different stocks
        st.sidebar.header("Comparison")
        tickers = st.sidebar.text_input(
            "Enter stock tickers for comparison (comma separated)", "TCS.NS, INFY.NS")
        tickers_list = [ticker.strip() for ticker in tickers.split(",")]

        if len(tickers_list) > 1:
            comparison_data = {}
            for t in tickers_list:
                comparison_data[t] = get_stock_data(
                    t, start_date, end_date)['Close']

            comparison_df = pd.DataFrame(comparison_data)
            st.subheader("Comparison of Stocks")
            st.line_chart(comparison_df)


if __name__ == "__main__":
    main()
