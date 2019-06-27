import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np


def calculate_conversion(revenue_target, conversion_rates, avg_revenue_customer):
    customers = revenue_target / avg_revenue_customer
    portal = customers / conversion_rates[2]
    web = portal / conversion_rates[1]
    impressions = web / conversion_rates[0]
    funnel = np.array([impressions, web, portal, customers]).astype(int)
    return funnel


impressions_web = 0.05
web_portal = 0.2
portal_customer = 0.6

conversion_rates = [impressions_web, web_portal, portal_customer]
avg_revenue_customer = 3225
revenue_target = 2000000

certification_funnel = calculate_conversion(revenue_target, conversion_rates, avg_revenue_customer)

funnel_index = ['Impressions', 'Web Visitors', 'New Portal Accounts', 'Customers']
column = ['Certification Funnel']
funnel_df = pd.DataFrame(data=certification_funnel,
                         index=funnel_index,
                         columns=column)


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='Funnel Calculator'),
    generate_table(funnel_df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
