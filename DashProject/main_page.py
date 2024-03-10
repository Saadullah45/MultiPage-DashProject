from dash import dcc, html
from dash.dependencies import Output, Input
from imports import data, app
from pages import univariate, bivariate

app.layout = html.Div(id='app_container', children=[
    html.Div(id='top_banner', children=[
        html.Img(src=app.get_asset_url('Dashboard_logo.png'))
    ]),
    html.Div([
        html.H1("Welcome to Suicide Analytical Dashboard",style={'textAlign': 'center'}),
        html.Hr(),
        html.H2("Types of Analysis"),
        html.Br(),
        dcc.Location(id='url'),  # for hyperlink, we need location to access the url
        dcc.Link("Univariate Analysis", href='/pages/univariate'),  # Text to display and the hyperlink
        html.Br(),
        dcc.Link("Bivariate Analysis", href='/pages/bivariate'),
        html.Div(id='page_content')
    ])
])

# Callback tells where should be the output and what would be the trigger behind
@app.callback(Output('page_content', 'children'),
              Input('url', 'pathname'))
def display_page_content(path):
    if path == '/pages/univariate':
        return univariate.layout
    elif path == '/pages/bivariate':
        return bivariate.layout
    else:
        return 'This is your homepage'

if __name__ == '__main__':
    app.run_server(debug=True)
