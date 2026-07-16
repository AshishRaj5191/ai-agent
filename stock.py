import requests
from config import FINNHUB_API_KEY

BASE_URL = "https://finnhub.io/api/v1/quote"


def execute(arguments: dict):

    symbol = arguments.get("symbol")

    if not symbol:
        return "Stock Error: Symbol is required."

    try:

        response = requests.get(
            BASE_URL,
            params={
                "symbol": symbol.upper(),
                "token": FINNHUB_API_KEY
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not data or data.get("c") == 0:
            return f"No stock data found for '{symbol}'."

        return (
            f"📈 Stock: {symbol.upper()}\n"
            f"💰 Current Price: ${data['c']}\n"
            f"📊 High: ${data['h']}\n"
            f"📉 Low: ${data['l']}\n"
            f"🟢 Open: ${data['o']}\n"
            f"🔴 Previous Close: ${data['pc']}"
        )

    except Exception as e:
        return f"Stock Error: {e}"


if __name__ == "__main__":

    print(
        execute(
            {
                "symbol": "TSLA"
            }
        )
    )