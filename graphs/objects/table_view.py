from pandas import DataFrame as df
from datetime import datetime

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from graphs.plotly_renders.covid_map import request_map
import requests, base64
from io import BytesIO
import dash_core_components as dcc
import plotly.graph_objs as go
from collections import Counter
from graphs.BadWayToRequestData.data import total
from graphs.BadWayToRequestData.mathdro import c_d_r_Stats, c_dates
from graphs.dtale_data.build_dtale import dtale_test
import dtale
import pandas as pd


def build_table(data=c_dates()):

    headers = []
    for x in data.head():
        print(data[x].name)
        headers.append(html.Th(data[x].name))

    table_header = [
        html.Thead(html.Tr(headers))
    ]

    table_values = []

    provinceState = c_dates()['provinceState'].values

    countryRegion = c_dates()['countryRegion'].values

    lastUpdate = c_dates()['lastUpdate'].values

    confirmed = c_dates()['confirmed'].values

    deaths = c_dates()['deaths'].values

    recovered = c_dates()['recovered'].values


    for p,region,l,c,d,r in zip(provinceState,countryRegion, lastUpdate, confirmed, deaths, recovered):
        table_values.append(html.Tr([html.Td(p), html.Td(region),  html.Td(l),  html.Td(c),  html.Td(d),  html.Td(r)]))
        # print(c_dates()[x].values)


    table = dbc.Row([dbc.Col(html.Div(), width=2), dbc.Col(dbc.Table(table_header + table_values, bordered=True)), dbc.Col(html.Div(), width=2)])

    return table

if __name__ == '__main__':
    print(build_table())