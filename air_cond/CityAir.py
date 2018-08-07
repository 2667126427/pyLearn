import json

import redis

import requests


class AirCond:
    post_url = 'http://epapi.moji.com/moji-epa/json/epa/cityStationList'
    air_para = {
        "common": {
            "platform": "Android",
            "language": "CN"
        },
        "params": {
            "cityId": ""
        }
    }

    def __init__(self, cityName):
        server = redis.Redis(host='47.100.124.50', port=6379)
        city_id = str(server.hget('city_list', cityName), encoding='utf8')
        if not city_id:
            raise Exception('Not valid city name: %s' % cityName)
        # city_info = json.loads(str(city_info,encoding='utf8'))
        self.air_para['params']['cityId'] = city_id

    def get_station(self):
        req = requests.post(self.post_url, json=self.air_para)
        return req.json(encoding='utf8')
