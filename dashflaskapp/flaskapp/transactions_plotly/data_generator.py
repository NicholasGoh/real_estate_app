'''Prepare data for Plotly Dash.'''
import pandas as pd

def load_transactions():
    return pd.read_csv('all_data/transactions/transactions_longlat.csv')
