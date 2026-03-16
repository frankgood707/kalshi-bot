import requests

url = "https://trading-api.kalshi.com/v1/markets"

def check_markets():
    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        markets = data.get("markets", [])

        for market in markets[:10]:
            ticker = market.get("ticker")
            yes_price = market.get("yes_bid")
            print(ticker, yes_price)

    except Exception as e:
        print("Connection failed:", e)

check_markets()
