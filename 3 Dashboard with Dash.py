import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

#Reading SpaceX csv
spacex = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
#Group by launch site
ls_sum = spacex.groupby("Launch Site").sum().reset_index()

#Creating Dash app
app = dash.Dash(__name__)

#App layout
app.layout = html.Div(children=[html.H1('LAB 3: SpaceX visualization in Dash', style={'textAlign': 'center','font-size': 40}),
                                html.P('Select a Launch Site:', style={'textAlign':'center'}),
                                dcc.Dropdown(id='site-dropdown',
                                             options=[{'label': 'All Sites', 'value': 'ALL'},
                                                      {'label': i, 'value': i} for i in ls_sum["Launch Site"]],
                                             value='ALL',
                                             placeholder="Select a Launch Site here",
                                             style={'font-size': '20px', 'text-align-last' : 'center'},
                                             searchable=True),])

#App callback
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    entered_site == 'ALL':
    fig = px.pie(spacex, values='class', names="Launch Site", title='Total sucess launches by site') 
    return fig

if __name__ == '__main__':
    app.run_server()
