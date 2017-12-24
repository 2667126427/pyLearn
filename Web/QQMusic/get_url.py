import re
import json
import time
import random
import requests
import urllib3

def resolve(url):
    """
    resolve audio url
    :param url: like 'https://y.qq.com/n/yqq/song/000YU69H3N55rZ.html'
    :return:
    """
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    songmid = re.search('/(\w+).html$', url).groups()[0]
    filename = 'C400' + songmid + '.m4a'
    guid = int(random.random() * 2147483647) * int(time.time() * 1000) % 10000000000

    d = {
        'format': 'json',
        'cid': 205361747,
        'uin': 0,
        'songmid': songmid,
        'filename': filename,
        'guid': guid,
    }

    r = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg', params=d, verify=False)
    vkey = json.loads(r.content)['data']['items'][0]['vkey']
    audio_url = 'http://dl.stream.qqmusic.qq.com/%s?vkey=%s&guid=%s&uin=0&fromtag=66' % (filename, vkey, guid)
    return audio_url

# print(resolve('https://y.qq.com/n/yqq/song/003OUlho2HcRHC.html'))
