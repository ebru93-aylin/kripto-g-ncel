
import requests
import pandas as pd
import time
import ta

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

def fetch_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=1&interval=hourly"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    # Teknik indikatörler
    df["rsi"] = ta.momentum.RSIIndicator(df["price"]).rsi()
    macd = ta.trend.MACD(df["price"])
    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()
    df["ao"] = ta.momentum.AwesomeOscillatorIndicator(df["price"], df["price"]).awesome_oscillator()

    return df.tail(1)  # Son 1 saatlik veriyi döndür

def fetch_all_data():
    frames = []
    for name, coin_id in coin_dict.items():
        df = fetch_coin_data(coin_id)
        if df is not None:
            df["coin"] = name
            frames.append(df)
        time.sleep(1.5)
    if frames:
        return pd.concat(frames)
    else:
        return pd.DataFrame()
