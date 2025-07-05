
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
        "BONK": "bonk"
    }

    ids = ','.join(coin_dict.values())
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"

    try:
        r = requests.get(url)
        r.raise_for_status()
        result = r.json()
    except Exception as e:
        print("API hatası:", e)
        return pd.DataFrame()

    rows = []
    for symbol, api_id in coin_dict.items():
        coin_data = result.get(api_id)
        if coin_data:
            usd = coin_data.get("usd", "N/A")
            change = coin_data.get("usd_24h_change", 0)
        else:
            usd = "N/A"
            change = 0
        rows.append({
            "Coin": symbol,
            "Fiyat (USD)": usd,
            "Change %": round(change, 2)
        })

    return pd.DataFrame(rows)
