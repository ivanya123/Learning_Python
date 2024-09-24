from dash import Dash, dcc, html
import pandas as pd


data = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [1, 2, 3, 4]
})

print(data.to_dict('records'))