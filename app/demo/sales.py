"""
Build a Python class called SalesAnalyzer that:
1. Loads sales data from a CSV file.
2. Provides methods to:
   - Get total sales
   - Get average sales per product
   - Get top N products by revenue
3. Handles exceptions for missing files or malformed data.
4. Uses matplotlib to plot a bar chart of the top N products.
5. file: ./sales_data.csv
"""


import pandas as pd
import matplotlib.pyplot as plt

class SalesAnalyzer:
    def __init__(self, csv_file):
        try:
            self.data = pd.read_csv(csv_file)
        except FileNotFoundError:
            print("File not found.")
            self.data = pd.DataFrame()
        except pd.errors.EmptyDataError:
            print("No data.")
            self.data = pd.DataFrame()
        except pd.errors.ParserError:
            print("Error parsing data.")
            self.data = pd.DataFrame()

    def get_total_sales(self):
        return self.data['revenue'].sum()

    def get_average_sales_per_product(self):
        return self.data.groupby('product_id')['revenue'].mean()

    def get_top_n_products(self, n=5):
        return self.data.groupby('product_id')['revenue'].sum().nlargest(n)

    def plot_top_n_products(self, n=5):
        top_products = self.get_top_n_products(n)
        top_products.plot(kind='bar')
        plt.title(f"Top {n} Products by Revenue")
        plt.xlabel("Product ID")
        plt.ylabel("Revenue")
        plt.show()

    def save_plot(self, filename):
        plt.savefig(filename)
