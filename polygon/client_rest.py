from polygon_rest import RESTClient
import datetime


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = "_t__ozhe3p5ACaYlHpPk2y4oEj7KkElP"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.reference_stock_financials("AAPL")



if __name__ == '__main__':
    main()