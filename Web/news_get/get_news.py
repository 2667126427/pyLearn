import requests
from bs4 import BeautifulSoup

illegals = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']


def get_links(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    _news_links = []
    for item in soup.select('.news-item'):
        if len(item.select('h2')) > 0:
            _news_links.append(item.select('a')[0]['href'])
    return _news_links


def get_details(url):
    detail = requests.get(url)
    detail.encoding = 'utf-8'
    _soup = BeautifulSoup(detail.text, 'html.parser')
    _title = _soup.select('title')[0].text
    body = _soup.select('#artibody')[0]
    _text = []
    for para in body.select('p'):
        _text.append(para.text.strip())
    _text = '\r\n    '.join(_text)
    for illegal in illegals:
        _title = _title.replace(illegal, ' ')
    _text = _text.replace(u'\xa0', u'').replace(u'\u2022', '*')
    return [_title, _text]


i = 0
news_links = get_links('http://news.sina.com.cn/china/')
for news in news_links:
    title, text = get_details(news)
    file_name = str(i + 1).zfill(2) + ' ' + title + '.txt'
    fw = open(file_name, 'w')
    fw.write(text)
    fw.close()
    i += 1
    print(file_name + ' was finished!')
print('All was finished. ' + str(i) + ' in total')
