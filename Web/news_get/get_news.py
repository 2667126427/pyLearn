from bs4 import BeautifulSoup
import requests


def get_url(page_url):
    news_url_list = []
    res = requests.get(page_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    for news in soup.select('.news-item'):
        if len(news.select('h2')) > 0:
            news_url_list.append(news.select('a')[0]['href'])
    return news_url_list


def get_details(news_url):
    res = requests.get(news_url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    if len(soup.select('#artibodyTitle')) > 0:
        title = soup.select('#artibodyTitle')[0].text.strip()
        content = soup.select('#artibody')[0].text.strip()
        time = soup.select('.time-source')[0].text.strip()
        return {time, title, content}
    else:
        return None

url = 'http://news.sina.com.cn/china/'
news_urls = get_url(url)
for news in news_urls:
    print(get_details(news))