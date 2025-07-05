
def generate_ai_signal(row):
    if row["Change %"] > 5:
        return "AL"
    elif row["Change %"] < -5:
        return "SAT"
    else:
        return "BEKLE"
