
import streamlit as st
from fetch_data import fetch_coin_data
from ai_module import generate_ai_signal

st.set_page_config(page_title="Kripto Sinyal Paneli", layout="wide")

st.title("📈 Kripto Sinyal Paneli")

coin_id = st.selectbox("Coin Seçiniz:", ["pepe", "floki", "dogecoin", "zksync", "ripple", "dogwifhat", "shiba-inu", "arbitrum", "bonk"])

if coin_id:
    data = fetch_coin_data(coin_id)
    market_data = data.get("market_data", {})
    current_price = market_data.get("current_price", {}).get("usd", "N/A")
    rsi = 45  # örnek değer
    macd = 5  # örnek değer

    signal = generate_ai_signal(rsi, macd)

    st.metric("Fiyat (USD)", current_price)
    st.metric("AI Sinyal", signal)
