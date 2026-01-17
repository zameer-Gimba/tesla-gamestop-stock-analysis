# Stock Data Extraction and Visualization

This project demonstrates how to extract, clean, and visualize
financial stock data using Python.

It combines API-based data extraction, web scraping, and interactive
visualization to explore historical stock prices and company revenues.

This work is part of my learning journey through the
**IBM Data Science Professional Certificate**.


## Overview

The project focuses on:
- Extracting historical stock prices using `yfinance`
- Scraping revenue data from publicly available sources
- Visualizing both metrics using interactive Plotly charts

Companies analyzed:
- Tesla (TSLA)
- GameStop (GME)


## Technologies Used

- Python
- Pandas
- yfinance
- BeautifulSoup
- Plotly
- Requests


## How to Run

### Option 1: Jupyter Notebook
Open the notebook file:
notebook/stock_data_visualization.ipynb

### Option 2: Python Script
Install dependencies:

```bash
pip install -r requirements.txt
```
Then import and use the function:
```
from src.stock_analysis import make_graph
```
### How to run tests:
```
python test.py
```
Note: Testing is optional for this project since the primary deliverable is a Jupyter Notebook with interactive visualizations.
