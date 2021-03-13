'''Prepare data for Plotly Dash.'''
import pandas as pd

def load_gdp():
    return pd.read_csv('all_data/macros/gdp.csv')
def load_hpi():
    return pd.read_csv('all_data/macros/hpi.csv')
def load_ir():
    return pd.read_csv('all_data/macros/ir.csv')
def load_flat_demand():
    return pd.read_csv('all_data/macros/flat_demand.csv')
