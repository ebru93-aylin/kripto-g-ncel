
# Kripto Sinyal Paneli

AI destekli, CoinGecko API ile canlı veri çeken, Telegram bildirimli Streamlit panel.

## Özellikler
- RSI, MACD gibi teknik analizler (genişletilebilir)
- AI sinyal tahmini: AL / SAT / BEKLE
- %5 değişimlerde Telegram mesajı
- Günlük veri analizi

## Çalıştırmak için
```
streamlit run app.py
```

## Telegram Bağlantısı
Streamlit Cloud -> Settings -> Secrets kısmına aşağıdaki gibi ekleyin:

```
TELEGRAM_TOKEN = "7757372996:AAGOzECzHvllRSWBZ_1h-JTmU4i58yMrDBA"
TELEGRAM_CHAT_ID = "694298537"
```
