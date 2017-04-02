import requests
from bs4 import BeautifulSoup
parser = 'html5lib'
arr_rep = ['<p>', '</p>', '<b>', '<pre>', '</pre>', '<div>', '</div>',
           '[<div id="problemContent">', ']', '<sub>', '</sub>']


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        full_name = 'PAT甲级1' + str(page).zfill(3) + '.txt'
        url = 'https://www.patest.cn/contests/pat-a-practise/1' + str(page).zfill(3)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, parser)
        text = str(soup.find('h1'))
        fw = open(full_name, 'w')
        text = text.replace('<h1>', '')
        text = text.replace('</h1>', '\n')
        fw.write(text)
        text = str(soup.find_all(id='problemContent'))
        text = text.replace('</b>', '\n')
        text = text.replace('&lt;', '<')
        for t in arr_rep:
            text = text.replace(str(t), '')
        fw.write(text)
        # print(text)
        fw.close()
        print(full_name + ' was done!')
        page += 1

trade_spider(60)
print('Done!')
'''
page = 53
full_name = 'PAT甲级1' + str(page).zfill(3) + '.txt'
url = 'https://www.patest.cn/contests/pat-a-practise/1' + str(page).zfill(3)
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, parser)
text = str(soup.find('h1'))
fw = open(full_name, 'w')
text = text.replace('<h1>', '')
text = text.replace('</h1>', '\n')
fw.write(text)
text = str(soup.find_all(id='problemContent'))
text = text.replace('</b>', '\n')
text = text.replace('&lt;', '<')
for t in arr_rep:
    text = text.replace(str(t), '')
print(text)
print(full_name + ' was done!')
'''