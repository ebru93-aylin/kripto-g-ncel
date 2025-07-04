
import requests
import pandas as pd
import time

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

def fetch_coin_data(coin_id, interval="1h"):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=1&interval=hourly"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        data = response.json()
        prices = data["prices"]
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df["price"] = df["price"].astype(float)
        df["rsi"] = df["price"].rolling(window=14).apply(lambda x: (x.diff().clip(lower=0).mean() / abs(x.diff()).mean()) * 100 if abs(x.diff()).mean() != 0 else 0)
        df["macd"] = df["price"].ewm(span=12).mean() - df["price"].ewm(span=26).mean()
        df["ao"] = df["price"].rolling(window=5).mean() - df["price"].rolling(window=34).mean()
        return df
    except Exception as e:
        print(f"Hata ({coin_id}):", e)
        return None

def fetch_all_data():
    results = []
    for symbol, coin_id in coin_dict.items():
        df = fetch_coin_data(coin_id)
        if df is not None and not df.empty:
            latest = df.iloc[-1]
            results.append({
                "Coin": symbol,
                "Kapanış Fiyatı ($)": round(latest["price"], 6),
                "RSI": round(latest["rsi"], 2) if pd.notna(latest["rsi"]) else "N/A",
                "MACD": round(latest["macd"], 6) if pd.notna(latest["macd"]) else "N/A",
                "AO": round(latest["ao"], 6) if pd.notna(latest["ao"]) else "N/A"
            })
        time.sleep(1.5)  # API rate limit için bekleme
    return pd.DataFrame(results)
