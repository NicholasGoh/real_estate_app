'''Instantiate a Dash app.'''
import numpy as np
import pandas as pd
import dash
import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc

# self packages
from .data_generator import load_gdp, load_hpi, load_ir, load_flat_demand
from .nav_bar import nav_bar_template

def init_dashboard(server):
    '''Create a Plotly Dash dashboard.'''
    dashApp = dash.Dash(
        server=server,
        routes_pathname_prefix='/macros/',
    )

    dashApp.index_string = nav_bar_template

    # Create Layout
    dashApp.layout = html.Div([
        # html.H1('Macro Dash Board', style={'text-align': 'center'}),
        html.Div([
            html.H2(children='Housing Price Index', style = {'text-align': 'left'}),
            html.Div(children=''' The House Price Index (HPI) is a broad measure of the movement of single-family house prices'''),
             html.Br(),
             dcc.Graph(id='Housing Price Index', figure={}),
             dcc.Slider(id='my-slider',min=0, max=184,
                marks={
                        0: {'label': '1975Q1'},
                        61: {'label': '1990Q1'},
                        122: {'label': '2005Q1'},
                        181: {'label': '2020Q1'}
                })
        ]),
         html.Div([
            html.H2(children='Gross Domestic Product', style = {'text-align': 'left'}),
            html.Div(children=''' Gross domestic product (GDP) is the total monetary or market value of all the finished goods and services produced within a country's borders in a specific time period.'''),
            html.Br(),
            dcc.Graph(id='GDP', figure={})
         ])
    ])

    @dashApp.callback(
        Output(component_id='Housing Price Index', component_property='figure'),
        Input(component_id='my-slider', component_property='value'),
    )

    def hpi_graph(value):
        hpi = load_hpi()
        dff = hpi.copy()
        dff_filtered = dff[:value]
        fig = px.line(dff_filtered, x='quarter', y= hpi.columns)
        return fig

    @dashApp.callback(
        Output(component_id='GDP', component_property='figure'),
        Input(component_id='GDP', component_property='figure'),
    )

    def gpd(figure):
        dff =  load_gdp()
        fig = px.line(dff, x='Quarter', y= dff.columns)
        return fig

    return dashApp.server

# @dashApp.callback(
    # Output(component_id='Housing Price Index', component_property='figure'),
    # Input(component_id='my-slider', component_property='value'),
# )

# def hpi_graph(value):
    # hpi = load_hpi()
    # dff = hpi.copy()
    # dff_filtered = dff[:value]
    # fig = px.line(dff_filtered, x='quarter', y= hpi.columns)
    # return fig

# @dashApp.callback(
    # Output(component_id='GDP', component_property='figure'),
    # Input(component_id='GDP', component_property='figure'),
# )

# def gpd(figure):
    # dff =  load_gdp()
    # fig = px.line(dff, x='Quarter', y= dff.columns)
    # return fig

# def create_data_table(df):
    # '''Create Dash datatable from Pandas DataFrame.'''
    # table = dash_table.DataTable(
        # id='database-table',
        # columns=[{'name': i, 'id': i} for i in df.columns],
        # data=df.to_dict('records'),
        # sort_action='native',
        # sort_mode='native',
        # page_size=300
    # )
    # return table
