import requests
import pandas as pd

from config import TWELVE_DATA_API_KEY

# ==========================
# BINANCE API (CRYPTO)
# ==========================

BINANCE_API = "https://api.binance.com/api/v3/klines"

# ==========================
# TWELVE DATA API
# ==========================

TWELVE_API = "https://api.twelvedata.com/time_series"


def get_crypto_data(symbol):
    """
    Download 1-minute crypto candles from Binance
    """

    symbol = symbol.replace("/", "")

    params = {
        "symbol": symbol,
        "interval": "1m",
        "limit": 100
    }

    try:
        response = requests.get(BINANCE_API, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

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

        df["time"] = pd.to_datetime(df["time"], unit="ms")

        for col in ["open", "high", "low", "close", "volume"]:
            df[col] = df[col].astype(float)

        return df

    except Exception as e:
        print(f"Crypto Error ({symbol}): {e}")
        return None


def get_forex_data(symbol):
    """
    Download 1-minute Forex/Gold/Silver candles from Twelve Data
    """

    params = {
        "symbol": symbol,
        "interval": "1min",
        "outputsize": 100,
        "apikey": TWELVE_DATA_API_KEY
    }

    try:
        response = requests.get(TWELVE_API, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "values" not in data:
            print(data)
            return None

        df = pd.DataFrame(data["values"])

        df = df.rename(columns={"datetime": "time"})

        for col in ["open", "high", "low", "close"]:
            df[col] = df[col].astype(float)

        if "volume" not in df.columns:
            df["volume"] = 0

        df["volume"] = df["volume"].astype(float)

        df = df[[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]]

        df = df.iloc[::-1].reset_index(drop=True)

        return df

    except Exception as e:
        print(f"Forex Error ({symbol}): {e}")
        return None
