import requests
import time

TOKEN = "8716947415:AAFz0eTvapxXcY4U-4gtpWxpEe_rodG8qSs"
CHAT_ID = "@michalltsch"

def send_signal():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    text = "🚀 БОТ РАБОТАЕТ!"
    requests.get(url, params={"chat_id": CHAT_ID, "text": text})

while True:
    send_signal()
    time.sleep(60)
