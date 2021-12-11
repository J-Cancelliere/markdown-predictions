"""Class to read sales data from csv and create a dataframe"""
import pandas as pd

class DataParser:
    
    def __init__(self,sales_data: pd.DataFrame):
        self.sales_data = sales_data

if __name__ == "__main__":
    print(__file__)
