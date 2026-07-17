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
