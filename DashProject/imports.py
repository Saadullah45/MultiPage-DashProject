import dash
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)
data=pd.read_csv('assets/Project Dataset Suicide.csv')
