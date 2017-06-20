import requests


_header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
name = 'chap{0}-{1}.jpg'


def download(chap, pic, res):
    file_name = name.format(str(chap).zfill(3), str(pic).zfill(2))
    fw = open(file_name, 'wb')
    fw.write(res.content)
    fw.close()
    print(file_name + ' was done!')


def __main__(start, end):
    url = 'http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%2F{0}%E8%AF%9D%2F{1}.jpg-dldl.middle'
    chap_url = 'http://www.douluodalu3.com/%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%E6%BC%AB%E7%94%BB/{0}.html'
    for chap in range(start, end + 1):
        res = requests.get(chap_url.format(chap), _header)
        for pic in range(1, 100):
            res = requests.get(url.format(str(chap).zfill(2), pic), _header)
            if res.status_code == 404:
                print(pic)
                break
            elif res.status_code == 200:
                download(chap, pic, res)
            else:
                print(res.status_code)

if __name__ == '__main__':
    start = input("Enter the start: ")
    end = input("Enter the end: ")

    __main__(int(start), int(end))
