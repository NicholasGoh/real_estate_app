'''Instantiate a Dash app.'''
import numpy as np
import pandas as pd
import dash
import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc

# self packages
from .data_generator import load_transactions
from .nav_bar import nav_bar_template

def init_transactions(server):
    '''Create a Plotly Dash dashboard.'''
    dashApp = dash.Dash(
        server=server,
        routes_pathname_prefix='/transactions/',
    )

    dashApp.index_string = nav_bar_template

    # Create Layout
    dashApp.layout = html.Div([
        html.H1('transactions', style={'text-align': 'center'}),
         html.Div([
            html.H2(children='Transactions Map', style = {'text-align': 'left'}),
            html.Div(children=''' map to visualize transactions '''),
            html.Br(),
            dcc.Graph(id='transactions_map', figure={})
         ]),
         # html.Div([
            # html.H2(children='comparisons', style = {'text-align': 'left'}),
            # html.Div(children='''stuff to compare'''),
            # html.Br(),
            # dcc.Graph(id='table_id', figure={})
         # ])
    ])

    @dashApp.callback(
        Output(component_id='transactions_map', component_property='figure'),
        Input(component_id='transactions_map', component_property='figure'),
    )

    def make_map(figure):
        transactions = load_transactions()
        fig = px.scatter_mapbox(transactions, lat='x', lon='y', hover_name='project', hover_data=['price', 'noOfUnits', 'propertyType', 'floorRange'],
                                color_discrete_sequence=['fuchsia'], zoom=12, height=450)
        fig.update_layout(mapbox_style='open-street-map')
        fig.update_layout(clickmode='event+select')
        fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})

        return fig

    @dashApp.callback(
        Output(component_id='transactions_map', component_property='children'),
        Input(component_id='transactions_map', component_property='clickData'),
    )
    def display_click_data(data):
        # all_click.append(data)
        print(data)

    # @dashApp.callback(
        # Output(component_id='table_id', component_property='figure'),
        # Input(component_id='table_id', component_property='value'),
    # )
    # def generate_table(value):
        # table =chunk(col())
        # table = chunk(row())
        # return table

    return dashApp.server
