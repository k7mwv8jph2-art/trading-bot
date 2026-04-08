import requests

TOKEN = "8716947415:AAFz0eTvapxXcY4U-4gtpWxpEe_rodG8qSs
"

# получаем данные
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
data = requests.get(url).json()

# берём chat id
chat_id = data["result"][-1]["message"]["chat"]["id"]

print("ТВОЙ CHAT_ID:", chat_id)
