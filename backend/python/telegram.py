import sys
import requests
from dotenv import find_dotenv, dotenv_values

SECRETS = dotenv_values(find_dotenv())

BOT_TOKEN = SECRETS.get('BOT_TOKEN')
CHAT_ID = SECRETS.get('CHAT_ID')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    x = requests.post(url, data=payload)
    print(x)

if len(sys.argv) > 1:
    send_telegram_message(sys.argv[1])