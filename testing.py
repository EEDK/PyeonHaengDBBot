import requests as req
from datetime import datetime
import json
import os
from dotenv import load_dotenv


load_dotenv()

# check 서버
baseURL = os.environ.get('baseURL')
webhook_url = os.environ.get('webhook_url')

headers = {
    "Content-Type": "application/json"
}


# 디스코드 메세지 전송 함수
def send_discord_message(msg):
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
    payload = {
        "content":
        msg + "\n" +
        today + "\n"
    }
    req.post(webhook_url, data=json.dumps(payload), headers=headers)


# 서비스 체크
try:
    r = req.get(
        baseURL + '/api/products/search?limit=20&event=All&order-by=none&offset=0&name=하겐&cvs=all')
    print(baseURL, 'return_code :', r.status_code)
except Exception as e:
    send_discord_message("@everyone 서버 살리세요")
