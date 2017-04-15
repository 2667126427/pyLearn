from bs4 import BeautifulSoup
import requests


def get_info(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    return req.text


def get_url(req):
    soup = BeautifulSoup(req, "html.parser")
    for item in soup.select('a'):
        yield item.text


def __main__():
    req = get_info("https://news.baidu.com")
    for text in get_url(req):
        print(text)

if __name__ == "__main__":
    __main__()