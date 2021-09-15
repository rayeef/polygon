import datetime

import pandas as pd
import json
from polygon_rest import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000000000.0).strftime('%Y-%m-%d %H:%M')

def Gainers():
    key = "_t__ozhe3p5ACaYlHpPk2y4oEj7KkElP"
    client = RESTClient(key)
    response = client.stocks_equities_snapshot_gainers_losers('gainers')
    print("TODAY'S TOP 20 GAINERS")
    df_gainers = pd.DataFrame(columns=['Symbol', 'Todays Change ($)', 'Change (%)'])
    for i in response.tickers:
        dt = ts_to_datetime(i['updated'])
        l = {'Symbol': i['ticker'], 'Todays Change ($)': i["todaysChange"], 'Change (%)': i["todaysChangePerc"]}
        df_gainers = df_gainers.append(l, ignore_index=True)
    print(df_gainers)


def Losers():
    key = "_t__ozhe3p5ACaYlHpPk2y4oEj7KkElP"
    client = RESTClient(key)
    response = client.stocks_equities_snapshot_gainers_losers('losers')
    print("TODAY'S TOP 20 LOSERS")
    df_losers = pd.DataFrame(columns=['Symbol', 'Todays Change ($)', 'Change (%)'])
    for i in response.tickers:
        dt = ts_to_datetime(i['updated'])
        l = {'Symbol': i['ticker'], 'Todays Change ($)': i["todaysChange"], 'Change (%)': i["todaysChangePerc"]}
        df_losers = df_losers.append(l, ignore_index=True)
    print(df_losers)

Gainers()
Losers()
