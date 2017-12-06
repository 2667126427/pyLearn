from bs4 import BeautifulSoup as Soup
import requests, sys


class Downloader(object):
    '''
    小说下载python程序
    '''
    def __init__(self):
        self.server = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.urls = []
        self.nums = 0
    
    def get_download_url(self):
        '''
        获取所有的下载链接
        '''
        req = requests.get(self.target)
        req.raise_for_status()
        html = req.text
        soup = Soup(html, 'html.parser')
        divs = soup.find_all('dd')
        divs = divs[15:]
        self.nums = len(divs)
        for div in divs:
            name = div.string
            href = self.server + div.find('a')['href']
            self.urls.append((name, href))

    def get_contents(self, target):
        '''
        获取链接中的小说内容
        '''
        req = requests.get(target)
        html = req.text
        soup = Soup(html, 'html.parser')
        text = soup.select('.showtxt')[0].text.replace('\xa0' * 8, '\n\n')
        return text

    def write(self, name, path, text):
        '''
        将文本写入文件
        '''
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = Downloader()
    dl.get_download_url()
    print('开始下载。。。\n')
    for i in range(dl.nums):
        nam, url = dl.urls[i]
        dl.write(nam, '一念永恒.txt', dl.get_contents(url))
        sys.stdout.write('已下载:%.3f%%' % float(i / dl.nums * 100) + '\r')
        sys.stdout.flush()
    print('下载完成。')
