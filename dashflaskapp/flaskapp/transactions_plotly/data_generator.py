import pandas as pd

# helper functions to load data easily in transactions dash app
def load_transactions():
    return pd.read_csv('all_data/transactions/transactions_longlat.csv')
def comparisons_df():
    data = {'x': [''],
            'y': [''],
            'price': [''],
            'noOfUnits': [''],
            'propertyType': [''],
            'floorRange': ['']
           }
    return pd.DataFrame.from_dict(data)
