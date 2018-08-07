import requests
from bs4 import BeautifulSoup
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}


def download_file(url, file):
    print(url)
    if '/' in file:
        dirc = file[:file.rfind('/')]
        if not os.path.exists(dirc):
            os.makedirs(dirc)
    with open(file, 'w', encoding='utf8')  as fp:
        fp.write(requests.get(url).text)
    print('download {} successfully'.format(file))


def download(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    body = soup.select_one('tbody')
    if body:
        trs = body.select('tr')[1:]
        for tr in trs:
            download('https://github.com' + tr.select_one('a.js-navigation-open')['href'])
    else:
        down = soup.select_one('#raw-url')
        if down:
            href = down['href']
            download_file('https://raw.githubusercontent.com' + href.replace('raw/', ''), href[href.find('master/') + 7:])


if __name__ == '__main__':
    url = 'https://github.com/apache/incubator-echarts/tree/master/map'
    download(url)
