import requests

from write_to_mongo import DBWriter

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
    json_data = req.json()
    for d in json_data['list']:
        writer = DBWriter(dbname='state',
                          coll=d['stationName'])
        writer.write_one(d)
    for d in json_data['nonStateList']:
        if d['aqi'] != -1:
            writer = DBWriter(dbname='nonstate',
                          coll=d['stationName'])
            writer.write_one(d)
