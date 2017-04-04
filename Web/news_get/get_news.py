import requests
from bs4 import BeautifulSoup


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
    return [_title, _text]


res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
news_links = []
for item in soup.select('.news-item'):
    if len(item.select('h2')) > 0:
        news_links.append(item.select('a')[0]['href'])

'''
title, text = get_details(news_links[0])
title = str(title).replace('|', ' ')
file_name = title + '.txt'
print(title)
print(text)
fw = open(file_name, 'w')
text.replace(u"\xa0", " ")
fw.write(text)
fw.close()
'''
i = 0
for news in news_links:
    try:
        title, text = get_details(news)
        title = str(title).replace('|', ' ')
        file_name = str(i + 1).zfill(2) + ' ' + title + '.txt'
        fw = open(file_name, 'w')
        text.replace(u"\xa0", " ")
        fw.write(text)
        fw.close()
        i += 1
        print(file_name + ' was finished!')
    except UnicodeEncodeError as err:
        print(err)
print('All was finished. ' + str(i) + ' in total')
