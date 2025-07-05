
import pandas as pd
import requests

def fetch_coin_data():
    coin_dict = {
        "PEPE": "pepe",
        "FLOKI": "floki",
        "DOGE": "dogecoin",
        "ZKSYNC": "zksync",
        "XRP": "ripple",
        "WIF": "dogwifhat",
        "SHIBA": "shiba-inu",
        "ARBITRUM": "arbitrum",
        "BONK": "bonk",
    }
    rows = []
    for symbol, api_id in coin_dict.items():
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={api_id}&vs_currencies=usd&include_24hr_change=true"
        r = requests.get(url)
        if r.status_code == 200:
            result = r.json()
            usd = result[api_id]["usd"]
            change = result[api_id].get("usd_24h_change", 0)
            rows.append({"Coin": symbol, "Fiyat (USD)": usd, "Change %": round(change, 2)})
        else:
            rows.append({"Coin": symbol, "Fiyat (USD)": "N/A", "Change %": 0})
    return pd.DataFrame(rows)
