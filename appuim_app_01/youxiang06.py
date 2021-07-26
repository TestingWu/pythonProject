import keyring
import yagmail
from imbox import Imbox
import requests
import time
password = keyring.get_password('88mail', 'test@88.com')

def get_verse():
    url = 'https://v2.jinrishici.com/one.json?client=browser-sdk/1.2&X-User-Token=xxxxxx'
    response = requests.get(url)
    return f'您要的每日诗句为：{response.json()["data"]["content"]}'

def get_weather(city):
    url = f'http://wthrcdn.etouch.cn/weather_mini?city={city}'
    response = requests.get(url).json()
    results = response['data']['forecast'][0]
    return f'{city}今天的天气情况为{results["type"]}，{results["high"][:-1]}度，{results["low"][:-1]}度'

def send_mail(email, results):
    mail = yagmail.SMTP(user='test@88.com', password=password, host='smtp.88.com')
    contents = [results]
    mail.send(email, '【自动回复】您要的信息见正文', contents)

def main():
    with Imbox('imap.88.com', 'test@88.com', password, ssl=True) as imbox:
        unread_inbox_messages = imbox.messages(unread=True)  # 获取未读邮件
        for uid, message in unread_inbox_messages:
            title = message.subject
            email = message.sent_from[0]['email']
            results = ''
            if title == '来句诗':
                results = get_verse()
            if title[-2:] == '天气':
                results = get_weather(title[:-2])
            if results:
                send_mail(email, results)
            imbox.mark_seen(uid)

while True:
    main()
    time.sleep(600)