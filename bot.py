import asyncio
import random
from datetime import datetime

from telegram import Bot

from config import (
    BOT_TOKEN,
    CHAT_ID,
    FOREX_PAIRS,
    CRYPTO_PAIRS,
    METALS,
    MIN_CONFIDENCE,
    TIMEFRAME,
)
bot = Bot(token=BOT_TOKEN)


def get_all_pairs():
    return FOREX_PAIRS + METALS + CRYPTO_PAIRS


def generate_signal():
    pair = random.choice(get_all_pairs())

    signal = random.choice(["BUY 🟢", "SELL 🔴"])

    confidence = random.randint(MIN_CONFIDENCE, 99)

    now = datetime.now()

    entry_time = now.strftime("%H:%M:%S")

    expiry = (now.replace(second=0, microsecond=0)
              + __import__("datetime").timedelta(minutes=1)).strftime("%H:%M")

    return pair, signal, confidence, entry_time, expiry
