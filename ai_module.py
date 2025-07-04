
def ai_signal(rsi, macd, ao, wavetrend):
    if rsi > 70 and macd == "SELL" and ao < 0:
        return "SAT", "Yüksek Risk"
    elif rsi < 30 and macd == "BUY" and ao > 0:
        return "AL", "Düşük Risk"
    else:
        return "BEKLE", "Orta Risk"
