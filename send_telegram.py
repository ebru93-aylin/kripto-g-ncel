
import requests

def send_signal_to_telegram(coin, signal, price, risk):
    TOKEN = "7757372996:AAGOzECzHvllRSWBZ_1h-JTmU4i58yMrDBA"
    CHAT_ID = "694298537"
    text = f"📈 {coin} | AI Sinyal: {signal}\n💰 Fiyat: ${price}\n⚠️ Risk: {risk}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})
