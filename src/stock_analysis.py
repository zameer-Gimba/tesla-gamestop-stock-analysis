"""
Stock Data Extraction and Visualization

This script extracts historical stock prices using yfinance,
retrieves company revenue data via web scraping, and visualizes
both using interactive Plotly charts.

Project completed as part of the IBM Data Science Professional Certificate.
"""

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def make_graph(stock_data, revenue_data, stock_name):
    """
    Creates an interactive Plotly chart showing:
    - Historical stock price
    - Historical revenue

    Parameters:
        stock_data (DataFrame): Stock price history
        revenue_data (DataFrame): Revenue history
        stock_name (str): Company name for title
    """

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=("Historical Share Price", "Historical Revenue"),
        vertical_spacing=0.3
    )

    # Limit data range for consistency
    stock_data = stock_data[stock_data["Date"] <= "2021-06-14"]
    revenue_data = revenue_data[revenue_data["Date"] <= "2021-04-30"]

    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(stock_data["Date"]),
            y=stock_data["Close"].astype(float),
            name="Share Price"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(revenue_data["Date"]),
            y=revenue_data["Revenue"].astype(float),
            name="Revenue"
        ),
        row=2,
        col=1
    )

    fig.update_yaxes(title_text="Price (USD)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue (USD Millions)", row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)

    fig.update_layout(
        title=stock_name,
        height=900,
        showlegend=False,
        xaxis_rangeslider_visible=True
    )

    fig.show()
