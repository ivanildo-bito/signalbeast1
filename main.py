from flask import Flask, request
import requests

app = Flask(_name_)

# Telegram bot gegevens
BOT_TOKEN = '7743716121:AAEtAuZPTaEqQK4lZysmMw6tV1Kv_K_NDyc'
CHAT_ID = '5952085659'  # Jouw chat ID

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=payload)

@app.route('/')
def home():
    return 'SignalBeast is online!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        message = f"Nieuw signaal ontvangen:\n\n{data}"
        send_telegram_message(message)
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
