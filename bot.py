import asyncio
from telegram import Bot

from config import (
    BOT_TOKEN,
    CHAT_ID,
    FOREX_PAIRS,
    CRYPTO_PAIRS,
    METALS,
)

from market_data import (
    get_crypto_data,
    get_forex_data,
)

from strategy import (
    calculate_indicators,
    generate_signal,
)

from signals import format_signal

bot = Bot(token=BOT_TOKEN)


def get_all_pairs():
    return FOREX_PAIRS + METALS + CRYPTO_PAIRS

# ← Leave one empty line here

async def analyze_pair(pair):
    ...
