import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

houses = pd.read_csv('Data/households.csv')
usage = pd.read_csv('Data/electricity_usage.csv')

merged = usage.merge(houses, on='house_id')

highest_consumption = merged.groupby('house_name')['units_consumed'].sum().reset_index()
highest_consumption.columns = ['House Name', 'Total Units']

monthly_trend = merged.groupby('month')['units_consumed'].sum().reset_index()
monthly_trend.columns = ['Month', 'Total Units']

average_usage = merged.groupby('house_name')['units_consumed'].mean().reset_index()
average_usage.columns = ['House Name', 'Average Units']
fig1 = px.bar(highest_consumption, x='House Name', y='Total Units',
              title='Highest Electricity Consumption by House',
              color='Total Units', text='Total Units')

fig2 = px.line(monthly_trend, x='Month', y='Total Units',
               title='Monthly Electricity Consumption Trend',
               markers=True)

fig3 = px.bar(average_usage, x='House Name', y='Average Units',
              title='Average Electricity Usage',
              color='Average Units', text='Average Units')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Electricity Consumption Dashboard', style={'textAlign':'center'}),
 html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3)
    ])
])

if __name__ == '__main__':
    app.run(debug=True)