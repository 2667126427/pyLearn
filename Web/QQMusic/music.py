import requests
from bs4 import BeautifulSoup as Soup
import key
import config
import get_url
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://y.qq.com/n/yqq/singer/0025NhlN2yWrP4.html#stat=y_new.singerlist.singername'
req = requests.get(url)
req.encoding = req.apparent_encoding
# print(req.text[:1000])
soup = Soup(req.text, 'html.parser')
songs = soup.find_all(name='span', attrs={'class': 'songlist__songname_txt'})
s = set()
for i in songs:
    url = 'https:' + i.find_all('a')[0]['href']
    name = i.text
    s.add((name + '.m4a', get_url.resolve(url)))

for name, url in s:
    req = requests.get(url)
    with open(name, 'wb') as f:
        f.write(req.content)
        print(name + "下载完成。")
