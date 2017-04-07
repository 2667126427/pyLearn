import requests
import random


def __main__():
    pages = range(1, 25)
    url = 'http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%2F01%E8%AF%9D%2F{}.jpg-dldl.middle'
    for page in pages:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                          '/57.0.2987.110 Safari/537.36'}
        response = requests.get(url.format(page), headers)
        file_name = str(page).zfill(2) + '.jpg'
        if response.status_code == 200:
            fw = open(file_name, 'wb')
            fw.write(response.content)
            fw.close()
            print(file_name, 'was done')
        else:
            print('get failed', page)


if __name__ == '__main__':
    __main__()
# 'http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%2F01%E8%AF%9D%2F2.jpg-dldl.middle'
# http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%2F01%E8%AF%9D%2F1.jpg-dldl.middle
# http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%2F01%E8%AF%9D%2F24.jpg-dldl.middle