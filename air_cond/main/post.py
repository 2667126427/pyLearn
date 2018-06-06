import json

import requests

from main.write_to_mongo import DBWriter

data = {
    "common": {
        "platform": "Android",
        "language": "CN",
    },
    "params": {
        "cityId": "310000"
    }
}

url = 'http://epapi.moji.com/moji-epa/json/epa/cityStationList'

if __name__ == '__main__':
    req = requests.post(url=url, json=data)
    json_data = json.loads(req.text)
    for d in json_data['list']:
        writer = DBWriter(host='47.100.124.50', dbname='state',
                          coll=d['stationName'])
        writer.write_one(d)
    for d in json_data['nonStateList']:
        writer = DBWriter(host='47.100.124.50', dbname='nonstate',
                          coll=d['stationName'])
        writer.write_one(d)
