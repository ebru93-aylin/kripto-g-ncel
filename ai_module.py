
def generate_ai_signal(rsi, macd):
    if rsi < 30 and macd > 0:
        return "AL"
    elif rsi > 70 and macd < 0:
        return "SAT"
    else:
        return "BEKLE"
