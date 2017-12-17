import requests
from bs4 import BeautifulSoup as Soup
import sys


# z_url = 'https://www.zhihu.com/question/31176110/answer/116496647'

def get_content(url):
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/62.0.3202.94 Safari/537.36'}

    req = requests.get(url, headers=head)
    req.raise_for_status()
    req.encoding = req.apparent_encoding

    soup = Soup(req.text, 'html.parser')

    content = soup.select('.RichContent-inner')[0]
    span = content.find('span')
    soup = Soup(span.prettify(), 'html.parser')
    return soup.text.replace('\n\n', '\n').replace('\n ', '\n').strip()


if __name__ == '__main__':
    url = str(sys.argv[1])
    content = get_content(sys.argv[1]) + '\n'
    index = url[url.rfind('/') + 1:]
    with open(index + '.txt', 'w') as f:
        f.write(content)
    print(content)