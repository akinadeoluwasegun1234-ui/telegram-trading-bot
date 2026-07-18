import pandas as pd
import ta


def calculate_indicators(df):
    """
    Calculate technical indicators
    """

    # EMA
    df["EMA20"] = ta.trend.ema_indicator(df["close"], window=20)
    df["EMA50"] = ta.trend.ema_indicator(df["close"], window=50)

    # RSI
    df["RSI"] = ta.momentum.rsi(df["close"], window=14)

    # MACD
    macd = ta.trend.MACD(df["close"])

    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()

    return df
    def generate_signal(df):
    """
    Generate a trading signal based on technical indicators.
    """

    last = df.iloc[-1]

    buy = (
        last["EMA20"] > last["EMA50"] and
        last["RSI"] > 55 and
        last["MACD"] > last["MACD_SIGNAL"]
    )

    sell = (
        last["EMA20"] < last["EMA50"] and
        last["RSI"] < 45 and
        last["MACD"] < last["MACD_SIGNAL"]
    )

    if buy:
        return "BUY", 85

    if sell:
        return "SELL", 85

    return "WAIT", 0
