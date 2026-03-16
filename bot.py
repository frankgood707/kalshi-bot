import requests
import time

API_KEY = "YOUR_API_KEY_HERE"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def check_markets():
    url = "https://api.kalshi.com/trade-api/v2/markets"
    r = requests.get(url, headers=headers)
    data = r.json()

    for market in data["markets"]:
        yes_price = market.get("yes_bid")

        if yes_price and yes_price < 30:
            print("Cheap YES contract:", market["ticker"], yes_price)

while True:
    check_markets()
    time.sleep(300)
