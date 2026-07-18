import requests

# Crypto
CRYPTO_API = "https://api.binance.com/api/v3/klines"

# Forex & Metals
FOREX_API = "https://api.twelvedata.com/time_series"

def get_crypto_data(symbol="BTCUSDT", interval="1m", limit=100):
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    r = requests.get(CRYPTO_API, params=params, timeout=10)
    return r.json()


def get_forex_data(symbol, api_key):
    params = {
        "symbol": symbol,
        "interval": "1min",
        "outputsize": 100,
        "apikey": api_key
    }

    r = requests.get(FOREX_API, params=params, timeout=10)
    return r.json()
