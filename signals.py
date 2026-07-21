from datetime import datetime, timedelta


def format_signal(pair, signal, confidence):
    entry = datetime.now()

    expiry = entry + timedelta(minutes=1)

    return f"""
🚀 JOHN AI TRADING SIGNAL

📊 Pair: {pair}

📈 Signal: {signal}

🎯 Confidence: {confidence}%

⏰ Entry Time: {entry.strftime("%H:%M:%S")}

⌛ Expiry Time: {expiry.strftime("%H:%M:%S")}

🕒 Timeframe: 1 Minute

⚠️ Risk only 1–2% of your account per trade.
"""
