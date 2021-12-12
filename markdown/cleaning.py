from markdown.parser import DataParser
import markdown.toolkit
import numpy as np
import pandas as pd

class CleanData:
    
    def __init__(self):
        self.sales_data = DataParser().read_sales_data()
    
    def get_clean_data(self):
        columns = list(self.sales_data.columns)
        data = self.sales_data.copy()
        for c in columns:
            data[c] = data[c].map(markdown.toolkit.make_dash_null)
            data[c] = data[c].map(markdown.toolkit.remove_percent)
            data[c] = data[c].map(markdown.toolkit.remove_euro)
            if c == "pvc_france":
                data[c] = data[c].map(markdown.toolkit.replace_commas)
            else:
                data[c] = data[c].map(markdown.toolkit.remove_comma)
            data[c] = pd.to_numeric(data[c], errors = "ignore")
        return data.dropna()
    
if __name__ == "__main__":
    print(CleanData().get_clean_data))