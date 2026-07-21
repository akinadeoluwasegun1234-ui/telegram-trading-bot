from datetime import datetime, timedelta


def format_signal(pair, signal, confidence):
    """
    Format Telegram signal message
    """

    entry_time = datetime.now()

    expiry_time = entry_time + timedelta(minutes=1)

    return f"""
🚀 <b>JOHN AI TRADING SIGNAL</b>

📊 <b>Pair:</b> {pair}

📈 <b>Signal:</b> {signal}

🎯 <b>Confidence:</b> {confidence}%

⏰ <b>Entry Time:</b> {entry_time.strftime("%H:%M:%S")}

⌛ <b>Expiry Time:</b> {expiry_time.strftime("%H:%M:%S")}

🕒 <b>Timeframe:</b> 1 Minute

⚠️ Risk only 1–2% of your account per trade.
"""
