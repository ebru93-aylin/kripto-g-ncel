
import streamlit as st
import pandas as pd
from fetch_data import fetch_all_data

st.set_page_config(page_title="Kripto Sinyal Paneli", layout="wide")

st.title("📊 Kripto Teknik Analiz Paneli")
st.markdown("Son 1 saatlik verilerle güncellenmiştir. RSI, MACD, AO göstergeleri yer almaktadır.")

with st.spinner("Veriler alınıyor..."):
    data = fetch_all_data()

if data is not None and not data.empty:
    st.dataframe(data, use_container_width=True)
else:
    st.warning("Veri alınamadı. Lütfen bağlantınızı kontrol edin veya daha sonra tekrar deneyin.")
