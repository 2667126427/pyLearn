import re
import requests


def get_html(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    if req:
        return req.text
    return None


def parse_html(html):
    print(html)
    pattern = re.compile('<dd><i.*?>(.*?)</i>.*?title="(.*?)".*?data-src="(.*?)".*?主演：(.*?)</p>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        print(item)
        yield {
            "rank": item[0],
            "title": item[1],
            "img_url": item[2],
            "actor": item[3]
        }


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_html(url)
    # print(html)
    print(html)
    pattern = re.compile('<dd><i.*?>(.*?)</i>.*?title="(.*?)" class.*?data-src="(.*?)".*?主演：(.*?)</p>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    for item in items:
        print(item)
        yield {
            "rank": item[0],
            "title": item[1],
            "img_url": item[2],
            "actor": item[3]
        }
    # parse_html(html)

if __name__ == '__main__':
    main(0)
