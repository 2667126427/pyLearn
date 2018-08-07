import redis
import json

if __name__ == '__main__':
    with open('city_list.json', 'r', encoding='utf8') as fp:
        city_list = json.loads(fp.read(), encoding='utf8')
    server = redis.Redis(host='47.100.124.50', port=6379)
    for city in city_list['list']:
        print(server.hset('city_list', city['fcityname'],
                          str(city['fcountryaqicode'])))
