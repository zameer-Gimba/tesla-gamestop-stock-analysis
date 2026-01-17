import unittest
import pandas as pd
from your_notebook_module import make_graph  # only if you refactor to .py

class TestStockGraph(unittest.TestCase):

    def test_make_graph_runs(self):
        stock_data = pd.DataFrame({
            "Date": ["2020-01-01", "2020-06-01"],
            "Close": [100, 200]
        })

        revenue_data = pd.DataFrame({
            "Date": ["2020-01-01", "2020-06-01"],
            "Revenue": [5000, 6000]
        })

        try:
            make_graph(stock_data, revenue_data, "TestStock")
            ran = True
        except Exception:
            ran = False

        self.assertTrue(ran, "make_graph should run without errors")

if __name__ == "__main__":
    unittest.main()
