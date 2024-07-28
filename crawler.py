import os
import requests
from bs4 import BeautifulSoup
import schedule
import time
from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv

load_dotenv()

# Line Bot API token
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
USER_ID = os.getenv('USER_ID')
KEYWORD = os.getenv('KEYWORD')

# line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# line_bot_api.broadcast(TextSendMessage(text='Hello World!'))

def send_line_notify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}'
    }
    data = {
        'message': message
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print('LINE通知發送成功')
        else:
            print(f'LINE通知發送失敗: {response.status_code}')
    except Exception as e:
        print(f'發送LINE通知時出錯: {e}')



def check_website():
    url = os.getenv('TARGET_WEBSITE_URL')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if KEYWORD in soup.text:
        send_line_notification(f'{KEYWORD} 出現了！')

def send_line_notification(message):
    # line_bot_api.push_message(USER_ID, TextSendMessage(text=message))
    line_bot_api.broadcast(TextSendMessage(text=message))

check_website()
# # 每小時執行一次 check_website 函數
# schedule.every().hour.do(check_website)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
