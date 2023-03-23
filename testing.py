import requests as req
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()

# check 서버
testURL = os.environ.get('testURL')
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


try:
    r = req.get(testURL, verify=False)
    print('ok')

except Exception as e:
    print(e)
    send_discord_message("@everyone 서버 살려주세요")
