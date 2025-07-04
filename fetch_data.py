
import requests

def fetch_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}?localization=false"
    response = requests.get(url)
    return response.json()
