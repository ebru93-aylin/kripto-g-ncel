
import streamlit as st
from fetch_data import fetch_coin_data
from ai_module import ai_signal
from send_telegram import send_signal_to_telegram

st.set_page_config(page_title="Kripto Sinyal Paneli", layout="wide")

st.title("📊 Kripto Sinyal Paneli (AI Destekli)")

data = fetch_coin_data()
st.dataframe(data)

for index, row in data.iterrows():
    ai_result, risk = ai_signal(row["RSI"], row["MACD"], row["AO"], row["WaveTrend"])
    st.write(f"{row['Coin']} - AI Sinyali: {ai_result} ({risk})")
    if row["Momentum Alarmı"] == "⚠️":
        send_signal_to_telegram(row['Coin'], ai_result, row['Kapanış Fiyatı ($)'], risk)
