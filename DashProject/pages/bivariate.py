# Bivariate.py
import pandas as pd
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from imports import data, app
import numpy as np

Yearly_data = data.pivot_table(index=['year'], values=['suicides_no', 'population', 'HDI for year', 'gdp_for_year'], aggfunc=np.sum)
fig1=px.bar(data, x=data['country'], color=data['generation'])

# Create a function to generate Trend line, scatter plot and cluster plot
def generate_bivariate_plots(selected_feature_trend, selected_feature_scatter, selected_feature_clusters):
    # Trend Line
    fig_trend = px.line(Yearly_data, x=Yearly_data.index, y=selected_feature_trend, title=f'{selected_feature_trend} Analysis Trendline')

    # Scatter
    fig_Scatter = px.scatter(data, x=data['suicides_no'], y=selected_feature_scatter, title=f'{selected_feature_scatter} Analysis - Scatter Plot')

    # Cluster
    fig_cluster = px.bar(data, x=selected_feature_clusters, color=data['generation'], title=f'{selected_feature_clusters} Analysis - Clustured Bar Chart')

    return fig_trend, fig_Scatter, fig_cluster

# Original bivariate layout with dropdowns
layout = html.Div([
    html.H1("Bivariate Analysis", style={'textAlign': 'center'}),
    html.Hr(),

    # First div for trendline
    html.Div([
        html.H2("Numerical Columns Analysis",style={'textAlign': 'center'}),
        html.H2("Trendline"),

        # Dropdown for trendline
        dcc.Dropdown(
            id='feature-dropdown-trend',
            options=[
                {'label': 'Suicide Number', 'value': 'suicides_no'},
                {'label': 'Population', 'value': 'population'},
                {'label': 'GDP', 'value': 'gdp_for_year'}
            ],
            value='suicides_no',  # Default selected value
        ),

        # Trendline component
        dcc.Graph(id='line_plot')
    ]),

    # Second div for scatter
    html.Div([
        html.H2("Scatter Plot"),
        # Dropdown for scatter
        dcc.Dropdown(
            id='feature-dropdown-scatter',
            options=[
                {'label': 'Population', 'value': 'population'},
                {'label': 'HDI Values', 'value': 'HDI for year'},
                {'label': 'GDP', 'value': 'gdp_for_year'}
            ],
            value='population',  # Default selected value
        ),

        # Scatter component
        dcc.Graph(id='scatter_plot')
    ]),
 # third div for Age Cluster
    html.Div([
        html.H2("Categorical Columns Analysis",style={'textAlign': 'center'}),
        html.H2("Clustured Bar Chart"),
        # Dropdown for scatter
        dcc.Dropdown(
            id='feature-dropdown-cluster',
            options=[
                {'label': 'Age and Gender', 'value': 'sex'},
                {'label': 'Age and Generation', 'value': 'generation'},
            ],
            value='sex',  # Default selected value
        ),

        # Scatter component
        dcc.Graph(id='cluster_plot')
    ]),

     # Forth div for scatter
    html.Div([
        html.H2("Stacked Bar Chart"),
        # Scatter component
        dcc.Graph(id='stacked_bar',
                  figure=fig1)
    ])


])

# Callback to update the line plot, scatter plot, and clustered bar chart based on the selected dropdown values
@app.callback(
    [Output('line_plot', 'figure'),
     Output('scatter_plot', 'figure'),
     Output('cluster_plot', 'figure')],
    [Input('feature-dropdown-trend', 'value'),
     Input('feature-dropdown-scatter', 'value'),
     Input('feature-dropdown-cluster', 'value')]
)
def update_graphs(selected_feature_trend, selected_feature_scatter, selected_feature_clusters):
    fig_trend, fig_scatter, fig_cluster = generate_bivariate_plots(
        selected_feature_trend, selected_feature_scatter, selected_feature_clusters
    )
    return fig_trend, fig_scatter, fig_cluster

