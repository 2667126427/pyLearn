import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html5lib')
    # print(str(soup))
    for post_text in soup.findAll('a', {'class': 'v-align-middle'}):
        content = post_text.string
        words = str(content).lower().split()
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)
    print(len(word_list))


start('https://github.com/search?utf8=%E2%9C%93&q=google&type=')

'''
<a href="/MarioVilas/google" class="v-align-middle">MarioVilas/<em>google</em></a>
'''