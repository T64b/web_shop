import time
from bot.handlers import bot_instance
from flask import Flask, abort
from flask import request
from bot.config import WEBHOOK_PREFIX, WEBHOOK_URL
from telebot.types import Update

app = Flask(__name__)


@app.route(WEBHOOK_PREFIX, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot_instance.process_new_updates([update])
        return '' # should return not None not False
    else:
        abort(403)


# убрать на верхний уровень
if __name__ == '__main__':
    bot_instance.remove_webhook()
    time.sleep(1)
    bot_instance.set_webhook(
        url=WEBHOOK_URL,
        certificate=open('webhook_cert.pem', 'r')
    )
    app.run(debug=True)
