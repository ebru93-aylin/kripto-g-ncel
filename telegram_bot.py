
import requests
import os

def send_telegram_message(message):
    token = os.getenv("TELEGRAM_TOKEN", "7757372996:AAGOzECzHvllRSWBZ_1h-JTmU4i58yMrDBA")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "694298537")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram gönderim hatası:", e)
