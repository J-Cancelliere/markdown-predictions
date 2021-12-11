"""Class to read sales data from csv and create a dataframe"""
import pandas as pd
import os

CSV_PATH = __file__[:-18] + "raw_data/"
CSV_NAMES = [f for f in os.listdir(CSV_PATH) if ".csv" in f]

class DataParser:
    
    def __init__(self):
        self.sales_data = pd.DataFrame
    
    def read_sales_data(self):
        dfs = []
        for f in CSV_NAMES:
            # Read DF from CSV file
            add_df = pd.read_csv(CSV_PATH + f)
            
            # Clean up and replace column names for each DF
            renamed_columns = []
            columns = list(add_df.columns)
            for c in columns:
                c = c.lower()
                c = c.replace("sem","")
                c = c.replace("\n","")
                c = c.replace("\r","")
                c = c.replace("+","")
                c = c.replace(".","")
                c = c.replace("-","_")
                c = c.replace(" ","_")
                c = c.replace("é","e")
                c = c.replace("è","e")
                renamed_columns.append(c)
            columns_dict = {c:r for c,r in zip(columns,renamed_columns)}
            add_df.rename(columns=columns_dict, inplace=True)
            
            # Drop the last row of the DF
            add_df.drop(add_df.tail(1).index, inplace = True)
        
            # Drop columns that are duplicated
            add_df.drop(columns=["tx_ecouln","defilementn"], errors = "ignore", inplace = True)
            
            # Add to list of DFs to concatenate
            dfs.append(add_df)
        self.sales_data = pd.concat(dfs)
        self.sales_data.reset_index(inplace = True)
        return self.sales_data

if __name__ == "__main__":
    print(DataParser().read_sales_data())
