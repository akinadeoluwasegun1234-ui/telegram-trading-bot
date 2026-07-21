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


async def analyze_pair(pair):
    # Get market data
    if pair in CRYPTO_PAIRS:
        df = get_crypto_data(pair)
    else:
        df = get_forex_data(pair)

    # No data received
    if df is None:
        return None

    # Empty dataframe
    if df.empty:
        return None

    # Calculate indicators
    df = calculate_indicators(df)

    # Not enough candles after indicator calculation
    if df.empty:
        return None

    # Generate signal
    signal, confidence = generate_signal(df)

    # Ignore WAIT signals
    if signal == "WAIT":
        return None

    # Format Telegram message
    return format_signal(pair, signal, confidence)


async def send_signal(pair):
    message = await analyze_pair(pair)

    if message:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode="HTML"
        )
        print(f"Signal sent: {pair}")


async def main():
    print("🚀 JOHN AI Trading Bot Started...")

    while True:
        print("🔍 Scanning market...")

        for pair in get_all_pairs():
            try:
                await send_signal(pair)
            except Exception as e:
                print(f"❌ Error with {pair}: {e}")

        print("✅ Scan complete. Waiting 60 seconds...\n")

        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())
