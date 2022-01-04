#import出現警告，要輸入路徑
#https://stackoverflow.com/questions/65252074/import-path-to-own-script-could-not-be-resolved-pylance-reportmissingimports

#ngork要放在程序包內
#打開cmd
#cd C:\Users\Chiang\Desktop\gitcode\Line_Bot\Line_Bot
#ngork http port



from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('62ujzaljiXLyJDBr/R7YM3QHnOkn153edo0Vxt8mqRcPQJNYNgxBSP6+SVolCV2iE0UygC9VJffUINuw757YoRtbHfHfRMrO/U0cuVHoblv+LRp/KDHBgW9tnVhQhZgbTsVHf0WKqsZb21agmAa/IQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ce53441f6aa752008763607c0ddb7d08')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return('OK')

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()