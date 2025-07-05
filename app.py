
import streamlit as st
from fetch_data import fetch_coin_data
from ai_module import generate_ai_signal
from telegram_bot import send_telegram_message
import pandas as pd

st.set_page_config(page_title="Kripto Sinyal Paneli", layout="wide")
st.title("📊 Kripto Sinyal Paneli - AI + Telegram")

data = fetch_coin_data()
st.dataframe(data)

for index, row in data.iterrows():
    signal = generate_ai_signal(row)
    st.write(f"{row['Coin']}: {signal}")
    if row['Change %'] >= 5 or row['Change %'] <= -5:
        send_telegram_message(f"{row['Coin']} fiyat hareketi: %{row['Change %']:.2f} — {signal}")
