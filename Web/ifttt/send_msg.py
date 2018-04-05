import threading
import requests
import time
import config
import json


def send_msg(**kwargs):
    url = 'https://maker.ifttt.com/trigger/{0}/with/key/{1}'.format(config.event, config.key)
    return requests.post(url, data=kwargs)


def get_price():
    url = 'https://api.coindesk.com/site/chartandheaderdata?currency=BTC'
    data = json.loads(requests.get(url).text)
    bpi = data['BTC']['header_data']['bpi']
    cny = bpi['CNY']['rate_float']
    usd = bpi['USD']['rate_float']
    print(cny, usd)
    return cny, usd


def update():
    cny, usd = get_price()
    print(send_msg(value1=cny, value2=usd))


if __name__ == '__main__':
    while True:
        update()
        // 休眠30分钟
        time.sleep(30 * 60)
