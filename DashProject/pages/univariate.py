# univariate.py
import pandas as pd
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from imports import data, app

# Create a function to generate box plot, histogram, bar chart, and pie chart
def generate_univariate_plots(selected_feature_box, selected_feature_hist, selected_feature_bar, selected_feature_pie):
    # Box plot
    fig_box = px.box(data, x=selected_feature_box, title=f'{selected_feature_box} Analysis - Box Plot')

    # Histogram
    fig_hist = px.histogram(data, x=selected_feature_hist, title=f'{selected_feature_hist} Analysis - Histogram')

    # Bar chart
    fig_bar = px.bar(data, x=selected_feature_bar, title=f'{selected_feature_bar} Analysis - Bar')

    # Pie chart
    fig_pie = px.pie(data, names=selected_feature_pie, title=f'{selected_feature_pie} Analysis - Pie')

    return fig_box, fig_hist, fig_bar, fig_pie

# Original univariate layout with dropdowns
layout = html.Div([
    html.H1("Univariate Analysis", style={'textAlign': 'center'}),
    html.Hr(),

    # First div for box plot
    html.Div([
        html.H2("Numerical Columns Analysis",style={'textAlign': 'center'}),
        html.H2("Box Plot"),

        # Dropdown for box plot
        dcc.Dropdown(
            id='feature-dropdown-box',
            options=[
                {'label': 'Suicide Number', 'value': 'suicides_no'},
                {'label': 'Year', 'value': 'year'},
                {'label': 'Population', 'value': 'population'},
                {'label': 'HDI Values', 'value': 'HDI for year'},
                {'label': 'GDP', 'value': 'gdp_for_year'}
            ],
            value='suicides_no',  # Default selected value
        ),

        # Box plot component
        dcc.Graph(id='box_plot')
    ]),

    # Second div for histogram
    html.Div([
        html.H2("Histogram"),
        # Dropdown for histogram
        dcc.Dropdown(
            id='feature-dropdown-hist',
            options=[
                {'label': 'Suicide Number', 'value': 'suicides_no'},
                {'label': 'Year', 'value': 'year'},
                {'label': 'Population', 'value': 'population'},
                {'label': 'HDI Values', 'value': 'HDI for year'},
                {'label': 'GDP', 'value': 'gdp_for_year'}
            ],
            value='suicides_no',  # Default selected value
        ),

        # Histogram component
        dcc.Graph(id='histogram')
    ]),

    # Third div for bar chart
    html.Div([
        html.H2("Categorical Columns Analysis",style={'textAlign': 'center'}),
        html.H2("Bar Chart"),
        # Dropdown for bar chart
        dcc.Dropdown(
            id='feature-dropdown-bar',
            options=[
                {'label': 'Generation', 'value': 'generation'},
                {'label': 'Age Groups', 'value': 'age'},
                {'label': 'Gender Ratio', 'value': 'sex'},
                {'label': 'Countries', 'value': 'country'},
            ],
            value='generation',  # Default selected value
        ),

        # Bar chart component
        dcc.Graph(id='barchart')
    ]),


    # Forth div for pie chart
    html.Div([
        html.H2("Pie Chart"),
        # Dropdown for pie chart
        dcc.Dropdown(
            id='feature-dropdown-pie',
            options=[
                {'label': 'Age Groups', 'value': 'age'},
                {'label': 'Gender Ratio', 'value': 'sex'},
                {'label': 'Generation', 'value': 'generation'},
                {'label': 'Countries', 'value': 'country'},
            ],
            value='age',  # Default selected value
        ),

        # Pie chart component
        dcc.Graph(id='piechart')
    ])

])

# Callback to update the box plot, histogram, bar chart, count plot, and pie chart based on the selected dropdown values
@app.callback(
    [Output('box_plot', 'figure'),
     Output('histogram', 'figure'),
     Output('barchart', 'figure'),
     Output('piechart', 'figure')
     ],
    [Input('feature-dropdown-box', 'value'),
     Input('feature-dropdown-hist', 'value'),
     Input('feature-dropdown-bar', 'value'),
     Input('feature-dropdown-pie', 'value')
     ]
)
def update_graphs(selected_feature_box, selected_feature_hist, selected_feature_bar, selected_feature_pie):
    fig_box, fig_hist, fig_bar, fig_pie = generate_univariate_plots(selected_feature_box, selected_feature_hist,
                                                                                selected_feature_bar, 
                                                                                selected_feature_pie)
    return fig_box, fig_hist, fig_bar,  fig_pie
