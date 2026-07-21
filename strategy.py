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

    # Remove rows with missing indicator values
    df = df.dropna()

    return df


def generate_signal(df):
    """
    Generate BUY / SELL / WAIT signal
    """

    last = df.iloc[-1]

    score = 0

    # EMA Trend
    if last["EMA20"] > last["EMA50"]:
        score += 30
    elif last["EMA20"] < last["EMA50"]:
        score -= 30

    # RSI
    if last["RSI"] > 55:
        score += 30
    elif last["RSI"] < 45:
        score -= 30

    # MACD
    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 30
    elif last["MACD"] < last["MACD_SIGNAL"]:
        score -= 30

    if score >= 60:
        return "BUY 🟢", min(score, 95)

    elif score <= -60:
        return "SELL 🔴", min(abs(score), 95)

    return "WAIT", abs(score)
