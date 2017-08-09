import os
import requests


# 想不到居然这样找到了链接
def get_picture_link(url):
    res = requests.get(url)
    text = res.text
    # 靠字符串搜索
    start_str = "g_img={url: \"/"
    start = text.find(start_str)
    end = text.find("\",id", start)
    result = url + text[start + len(start_str) - 1:end]
    print("Find the url: " + result)
    return result


def save_picture(link):
    res = requests.get(link)
    link = str(link)
    last = link.rfind("/")
    # 让名字好看一点
    _index = link.find("_")
    f_name = link[last + 1: _index] + ".jpg"
    # 判断文件是否存在
    if os.path.exists(f_name):
        print(f_name + " has existed")
    else:
        # 不存在就保存一下吧
        fout = open(f_name, "wb")
        fout.write(res.content)
        fout.close()
        print(f_name + " was downloaded successfully")


if __name__ == '__main__':
    # bing的首页地址
    url = "http://www.bing.com"
    link = get_picture_link(url)
    save_picture(link)
