import pandas as pd
import dash
from dash.dependencies import Input, Output, State
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

# self packages
from .data_generator import load_transactions, comparisons_df
from .nav_bar import nav_bar_template

all_click = []

transactions = load_transactions()
filter_options = {}
cols_for_filter = ['region', 'street', 'propertyType', 'tenure', 'project']
for col in cols_for_filter:
    col_options = []
    unique_values = transactions[col].unique()
    col_options.append({'label': 'All', 'value': 'All'})
    for val in unique_values:
        col_options.append({'label': val, 'value': val})
    filter_options[col] = col_options


# takes in preprocessed click data from the maps and returns the html table rendered version
# note default is invisible table
def render_table(click_data = None, default=False, max_rows=26):
    if default:
        return html.Table(
            id = 'comparison_table'
        )
    df = comparisons_df()
    click_data = click_data[-4:]
    for data in click_data:
        df = df.append(data)
    df.index = [[f'Property {i}' for i in range(len(df))]]
    rownames = df.columns
    df = df.T
    df['info'] = rownames
    df.drop(columns=['Property 0'], inplace=True)
    columns = list(df.columns)
    columns = columns[-1:] + columns[:-1]
    df = df[columns]
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns]) ] +
        # Body
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(min(len(df), max_rows))],
        id = 'comparison_table',
        className = 'table table-bordered active'
    )

# inits transactions dash app that links to flask app
def init_transactions(server):
    dashApp = dash.Dash(
        server=server,
        routes_pathname_prefix='/transactions/',
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    dashApp.index_string = nav_bar_template

    # Create Layout
    dashApp.layout = html.Div([
        html.H1('Transactions Dashboard', style={'text-align': 'center'}),
        html.Div([
            html.H2(children='Transactions Map', style = {'text-align': 'left'}),
            html.Div(children=''' map to visualize transactions '''),
            html.Br(),
            html.Div([
                dcc.Dropdown(
                    id='regionDropdown',
                    options = filter_options['region'],
                    value = 'All',
                    placeholder='Select a regiion'
                ),
                dcc.Dropdown(
                    id='streetDropdown',
                    options = filter_options['street'],
                    value = 'All',
                    placeholder='Select a street'
                ),
                dcc.Dropdown(
                    id='propertyTypeDropdown',
                    options = filter_options['propertyType'],
                    value = 'All',
                    placeholder='Select a property type'
                ),
                dcc.Dropdown(
                    id='tenureDropdown',
                    options = filter_options['tenure'],
                    value = 'All',
                    placeholder='Select length of tenure'
                ),
                dcc.Dropdown(
                    id='projectDropdown',
                    options = filter_options['project'],
                    value = 'All',
                    placeholder='Select a project'
                ),
                html.Button('Search', id='search-filter')
            ]),
            html.Br(),
            dcc.Loading(
                id = 'loading-map',
                type = 'default',
                children = dcc.Graph(id='transactions_map', figure={})
            )
        ]),
        html.Div(
            children = render_table(default=True),
            id = 'comparison_table_div',
        ),
        html.Div(id='hidden-container')
    ], className = 'container')


    @dashApp.callback(
        Output(component_id='transactions_map', component_property='figure'),
        [
            Input(component_id='search-filter', component_property='n_clicks'),
            Input(component_id='transactions_map', component_property='figure'),
        ],
        [
            State(component_id='regionDropdown', component_property='value'),
            State(component_id='streetDropdown', component_property='value'),
            State(component_id='propertyTypeDropdown', component_property='value'),
            State(component_id='tenureDropdown', component_property='value'),
            State(component_id='projectDropdown', component_property='value'),
        ]
    )

# debug here, add additional arguements to function
    def make_map(n_clicks, figure, region, street, propertyType, tenure, project):
        transactions = load_transactions()
        filters = [region, street, propertyType, tenure, project]

        for i in range(len(cols_for_filter)):
            if filters[i] != 'All':
                transactions = transactions[transactions[cols_for_filter[i]] == filters[i]]
        if transactions.empty:
            fig = px.scatter_mapbox(lat=['1.3521'], lon=['103.8198'])
        else:
            fig = px.scatter_mapbox(transactions, lat='x', lon='y', hover_name='project', hover_data=['price', 'region', 'street', 'area'],
                                    custom_data=['noOfUnits', 'propertyType', 'floorRange', 'project', 'tenure'], zoom=12, height=450)
        fig.update_layout(mapbox_style='open-street-map')
        fig.update_layout(clickmode='event+select')
        fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
        return fig

    @dashApp.callback(
        Output(component_id='comparison_table_div', component_property='children'),
        Input(component_id='transactions_map', component_property='clickData'),
    )
    
    def display_click_data(click):
        if click is None:
            return render_table(default=True)
        # preprocess the click data from maps
        points = click['points'][0]
        customdata = points['customdata']
        print(points)
        print(customdata)
        data = {
                'x': points['lat'],
                'y': points['lon'],
                'noOfUnits': customdata[0],
                'propertyType': customdata[1],
                'floorRange': customdata[2],
                'project': customdata[3],
                'tenure': customdata[4],
                'price': customdata[5],
                'region': customdata[6],
                'street': customdata[7],
                'area': customdata[8]
               }
        data = {k: [str(v)] for k, v in data.items()}
        data = pd.DataFrame.from_dict(data)
        all_click.append(data)
        return render_table(click_data=all_click)

    return dashApp.server
