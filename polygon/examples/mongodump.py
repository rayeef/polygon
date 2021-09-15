''' This code connects to Polygon's server via REST API to fetch & store historical data for a
given equity. at the moment only single equity is supported. Data is stored to MongoDB Cluster '''

import json
import bson
import pymongo
from pymongo import MongoClient
from polygon_rest import RESTClient
import datetime


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = "_t__ozhe3p5ACaYlHpPk2y4oEj7KkElP"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        from_ = "2000-01-01"
        to = "2021-09-01"
        resp = client.stocks_equities_aggregates("AAPL", 1, "day", from_, to, unadjusted=False)
        print(f"Day aggregates for {resp.ticker} between {from_} and {to}.")

        for result in resp.results:
            dt = ts_to_datetime(result["t"])
            jmsg = {"  Date":   dt,
                    "  Open":   result['o'],
                    "  High":   result['h'],
                    "  Low":    result['l'],
                    "  Close":  result['c'],
                    "  Volume": result['v']}

            '''BSON Verification  - expected output must be binary'''
            bmsg = bson.BSON.encode(jmsg)
            #print(bmsg)

            '''MongoDB Connection Link'''
            connection_string = "mongodb+srv://skhan:A330airbus@cluster0.f4uut.mongodb.net/POLYGON_STOCKS_EOD?retryWrites=true&w=majority"
            client = MongoClient(connection_string)
            db = client["POLYGON_STOCKS_EOD"]
            collection = db["AAPL"]
            collection.insert_one(jmsg)


if __name__ == '__main__':
    main()
