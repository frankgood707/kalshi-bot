import requests

url = "https://trading-api.kalshi.com/v1/markets"

def check_markets():
    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        markets = data.get("markets", [])

    for market in markets[:50]:
    ticker = market.get("ticker")
    yes_price = market.get("yes_bid")

    if yes_price and yes_price < 20:
        print("CHEAP CONTRACT:", ticker, yes_price)
