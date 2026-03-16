import requests
import os

API_KEY = os.getenv("KALSHI_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

url = "https://api.kalshi.com/trade-api/v2/markets"

def check_markets():
    r = requests.get(url, headers=headers)
    data = r.json()

    markets = data.get("markets", [])

    for market in markets[:10]:
        ticker = market.get("ticker")
        yes_price = market.get("yes_bid")

        print(ticker, yes_price)

        if yes_price and yes_price < 20:
            print("Possible BUY:", ticker)

check_markets()
