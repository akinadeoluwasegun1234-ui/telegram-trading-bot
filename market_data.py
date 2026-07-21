import requests
import pandas as pd

from config import TWELVE_DATA_API_KEY

# Binance API (Crypto)
BINANCE_API = "https://api.binance.com/api/v3/klines"

# Twelve Data API (Forex & Metals)
TWELVE_API = "https://api.twelvedata.com/time_series"


def get_crypto_data(symbol):
    symbol = symbol.replace("/", "")

    params = {
        "symbol": symbol,
        "interval": "1m",
        "limit": 100
    }

    r = requests.get(BINANCE_API, params=params)

    data = r.json()

    if not isinstance(data, list):
        return None

    df = pd.DataFrame(data)

    df = df.iloc[:, :6]

    df.columns = [
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    df = df.astype(float)

    return df


def get_forex_data(symbol):
    symbol = symbol.replace("/", "")

    params = {
        "symbol": symbol,
        "interval": "1min",
        "outputsize": 100,
        "apikey": TWELVE_DATA_API_KEY
    }

    r = requests.get(TWELVE_API, params=params)

    data = r.json()

    if "values" not in data:
        return None

    df = pd.DataFrame(data["values"])

    df = df.rename(columns={
        "datetime": "time"
    })

    df = df[[
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]]

    df[["open", "high", "low", "close", "volume"]] = df[
        ["open", "high", "low", "close", "volume"]
    ].astype(float)

    return df
