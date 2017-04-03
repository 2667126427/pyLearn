from urllib import request
import urllib.parse


def get_picture(img_url):

    name = "1.jpg"
    request.urlretrieve(img_url, name)


get_picture('http://mhpic.zymkcdn.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%2F01%E8%AF%9D%2F1.jpg-dldl.middle')
