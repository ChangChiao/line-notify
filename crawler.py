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

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
line_bot_api.broadcast(TextSendMessage(text='Hello World!'))

# def check_website():
#     url = os.getenv('TARGET_WEBSITE_URL')
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     if KEYWORD in soup.text:
#         send_line_notification(f'{KEYWORD} 出現了！')

# def send_line_notification(message):
#     # line_bot_api.push_message(USER_ID, TextSendMessage(text=message))
#     line_bot_api.broadcast(TextSendMessage(text=message))

# # 每小時執行一次 check_website 函數
# schedule.every().hour.do(check_website)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
