import requests
import time

url = "https://api.kalshi.com/trade-api/v2/markets"

def check_markets():
    try:
        r = requests.get(url)
        data = r.json()

        markets = data.get("markets", [])

        for market in markets[:10]:
            ticker = market.get("ticker")
            yes_price = market.get("yes_bid")

            print(ticker, yes_price)

    except Exception as e:
        print("Error:", e)

check_markets()
