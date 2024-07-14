# Stock Market Analysis App

This is a Streamlit-based web application for analyzing and visualizing stock market data. The app allows users to view stock price trends, candlestick charts, daily returns, and compare different stocks. Users can also see the percentage return for a specific year.

## Features

- Line charts showing stock price trends
- Candlestick charts for daily price movements
- Daily returns visualization
- Comparison of different stocks
- Percentage return for a selected year

## Installation

To run this app locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/Abhijnan18/DSV-Project.git
cd DSV-Project
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Usage

1. Open your web browser and go to `http://localhost:8501` (or the specified address and port in your `config.toml`).

2. Use the sidebar to enter the stock ticker (e.g., `TCS.NS`), select the start and end dates for the data, and choose the year for percentage return calculation.

3. View the various visualizations and analyses provided by the app.


## Dependencies

- streamlit==1.23.1
- yfinance==0.2.26
- pandas==1.5.3
- plotly==5.9.0
