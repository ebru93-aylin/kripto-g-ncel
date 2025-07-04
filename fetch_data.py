
import pandas as pd

def fetch_coin_data():
    # Gerçek API entegrasyonu CoinGecko ile yapılacak
    data = {
        "Coin": ["PEPE", "FLOKI", "DOGE"],
        "Kapanış Fiyatı ($)": [0.0000098, 0.000076, 0.123],
        "RSI": [35, 55, 78],
        "MACD": ["BUY", "SELL", "SELL"],
        "AO": [0.001, -0.002, -0.003],
        "WaveTrend": [55, 45, 70],
        "Momentum Alarmı": ["", "⚠️", "⚠️"],
    }
    return pd.DataFrame(data)
