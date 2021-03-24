import dash
from dash.dependencies import Input, Output
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

# self packages
from .data_generator import load_gdp, load_hpi, load_ir, load_flat_demand, load_transactions
from .nav_bar import nav_bar_template

# inits dash app for macros, linked to flask app
def init_macros(server):
    '''Create a Plotly Dash dashboard.'''
    dashApp = dash.Dash(
        server=server,
        routes_pathname_prefix='/macros/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    dashApp.index_string = nav_bar_template

    # Create Layout
    dashApp.layout = html.Div([
        html.H1("Macro Dash Board", style={'text-align': 'center'}),
        html.Div([
            html.H2(children='Housing Price Index', style={'text-align': 'left'}),
            html.Div(children=''' The House Price Index (HPI) is a broad measure of the movement of single-family house prices'''),
            html.Br(),
            dcc.Loading(
                children = [dcc.Graph(id='Housing Price Index', figure={}), 
                            dcc.Slider(id='my-slider', min=0, max=184,
                                        marks={
                                            0: {'label': '1975Q1'},
                                            61: {'label': '1990Q1'},
                                            122: {'label': '2005Q1'},
                                            181: {'label': '2020Q1'}
                                        })],
                type = 'default'
            ),
        ]),
        html.Div([
            html.H2(children='Gross Domestic Product',
                    style={'text-align': 'left'}),
            html.Div(children=''' Gross domestic product (GDP) is the total monetary or market value of all the finished goods and services produced within a country's borders in a specific time period.'''),
            html.Br(),

            dcc.Loading(
                children = [dcc.Checklist(id="select_industry",
                                options=[
                                    {"label": "Total GDP", "value": "Total_GDP"},
                                    {"label": "Goods Producing Industries",
                                    "value": "Goods_Producing_Industries"},
                                    {"label": "Construction", "value": "Construction"},
                                    {"label": "Utilities", "value": "Utilities"},
                                    {"label": "Wholsale Retail Trade",
                                    "value": "Wholesale_Retail_Trade"},
                                    {"label": "Transportation Storage",
                                    "value": "Transportation_Storage"},
                                    {"label": "Accomodation Food Services",
                                    "value": "Accommodation_Food_Services"},
                                    {"label": "Information Communication",
                                    "value": "Information_Communications"},
                                    {"label": "Finance Insurance",
                                        "value": "Finance_Insurance"},
                                    {"label": "Real Estate", "value": "Real_Estate"}],

                                value=["Quarter", "Total_GDP"],
                            ),
                            dcc.Graph(id='GDP', figure={}),
                            dcc.Slider(id='gdp_slider', min=0, max=184,
                                marks={
                                    0: {'label': '1975Q1'},
                                    61: {'label': '1990Q1'},
                                    122: {'label': '2005Q1'},
                                    181: {'label': '2020Q1'}
                                })],
                type = 'default'
            ),

        ]),
        html.Div([
            html.H2(children='Interest Rates', style={'text-align': 'left'}),
            html.Div(children='''An interest rate is the amount of interest due per period, as a proportion of the amount lent, deposited or borrowed. '''),
            html.Br(),
            dcc.Loading(
                children = [dcc.Checklist(id="select_ir",
                                options=[
                                    {"label": "Prime Lending Rate",
                                    "value": "Prime Lending Rate"},
                                    {"label": "3-month Fixed Deposit Rate",
                                    "value": "3-month Fixed Deposit Rate"},
                                    {"label": "6-month Fixed Deposit Rate",
                                    "value": "6-month Fixed Deposit Rate"},
                                    {"label": "12-month Fixed Deposit Rate",
                                    "value": "12-month Fixed Deposit Rate"},
                                    {"label": "Savings Deposit Rate", "value": "Savings Deposit Rate"}, ],

                                value=["Date", "Prime Lending Rate"],
                            ),
                            dcc.Graph(id='IR', figure={}),
                            dcc.Slider(id='ir_slider', min=0, max=457,
                                marks={
                                    0: {'label': '1983-Jan'},
                                    147: {'label': '1995-Jan'},
                                    304: {'label': '2008-Jan'},
                                    457: {'label': '2021-Jan'}
                                })],
                type = 'default'
            ),
        ]),

        html.Div([
            html.H2(children='Flat Demand', style={'text-align': 'left'}),
            html.Div(
                 children=''' Demand for rental and purchase of flat in a period of time '''),
            html.Br(),
            dcc.Loading(
                children = dcc.Graph(id='demand', figure={}),
                type = 'default'
            )

        ]),

        html.Div([
            html.H2(children='Transaction', style={'text-align': 'left'}),
            html.Div(children=''' URA Transacted housing price trend '''),
            html.Br(),
            html.Div(children=''' Property Type: '''),

            dcc.Loading(
                children = [dcc.RadioItems(id="propertyType",
                                options=[
                                    {'label': 'Condominium', 'value': 'Condominium'},
                                    {'label': 'Detached', 'value': 'Detached'},
                                    {'label': 'Apartment', 'value': 'Apartment'},
                                    {'label': 'Terrace', 'value': 'Terrace'},
                                    {'label': 'Semi-detached', 'value': 'Semi-detached'},
                                    {'label': 'Strata Terrace', 'value': 'Strata Terrace'},
                                    {'label': 'Strata Detached', 'value': 'Strata Detached'},
                                    {'label': 'Strata Semi-detached',
                                        'value': 'Strata Semi-detached'},
                                ], value='Condominium'),
                            html.Br(),
                            html.Div(children=''' Tenure: '''),
                            dcc.RadioItems(id="tenure",
                                options=[
                                    {'label': '99-years', 'value': '99-years'},
                                    {'label': 'Freehold', 'value': 'Freehold'},
                                    {'label': '999-years', 'value': '999-years'},
                                    {'label': '9999-years', 'value': '9999-years'},
                                ], value='99-years'),
                            html.Br(),
                            html.Div(children=''' District: '''),
                            dcc.Checklist(id="district",
                                options=[
                                    {"label": "1", "value": 1},
                                    {"label": "2", "value": 2},
                                    {"label": "3", "value": 3},
                                    {"label": "4", "value": 4},
                                    {"label": "5", "value": 5},
                                    {"label": "6", "value": 6},
                                    {"label": "7", "value": 7}, 
                                    ], value=[1]),
                            dcc.Graph(id='transac', figure={})],
                type = 'default'
            ),
            
        ])
    ], className = 'container')

    @dashApp.callback(
        Output(component_id='Housing Price Index', component_property='figure'),
        Input(component_id='my-slider', component_property='value'),
    )
    def hpi_graph(value):
        dff = load_hpi()
        dff_filtered = dff[:value]
        fig = px.line(dff_filtered, x='quarter', y=load_hpi().columns)
        return fig


    @dashApp.callback(
        Output(component_id='GDP', component_property='figure'),
        [Input(component_id='select_industry', component_property='value'),
         Input('gdp_slider', 'value')]
    )
    def gpd(value, gdp_slider):
        dff = load_gdp()
        filtered_industry = dff[value]
        filtered = filtered_industry[:gdp_slider]
        fig = px.line(filtered, x='Quarter', y=filtered.columns)
        return fig


    @dashApp.callback(
        Output(component_id='IR', component_property='figure'),
        [Input(component_id='select_ir', component_property='value'),
         Input('ir_slider', 'value')]
    )
    def interest_rate(value, ir_slider):
        dff = load_ir()
        filtered_ir = dff[value]
        filtered = filtered_ir[:ir_slider]
        fig = px.line(filtered, x='Date', y=filtered.columns)
        return fig


    @dashApp.callback(
        Output(component_id='demand', component_property='figure'),
        Input(component_id='demand', component_property='figure'),
    )
    def demand(figure):
        fig = px.line(load_flat_demand(), x='period', y=load_flat_demand().columns)
        return fig


    @dashApp.callback(
        Output(component_id='transac', component_property='figure'),

        [Input(component_id='propertyType', component_property='value'),
         Input(component_id='tenure', component_property='value'),
         Input(component_id='district', component_property='value'),
         Input(component_id='transac', component_property='figure')]
    )
    def transac(propType, tenure, dist, figure):
        dff = load_transactions()
        fpt = dff[dff['propertyType'] == propType]
        ft = fpt[fpt["tenure"] == tenure]
        fd = ft[ft["district"].isin(dist)]
        new_df = fd.groupby(by=["contractDate"], as_index=False).mean()
        new_df['contractDate'] = pd.to_datetime(new_df['contractDate'])
        new_df_sort = new_df.sort_values(by='contractDate')
        fig = px.line(new_df_sort, x="contractDate", y='per_meter_square')
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Mean Property Price Per Meter Squared")
        return fig

    return dashApp.server
