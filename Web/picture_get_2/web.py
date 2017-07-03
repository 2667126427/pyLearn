import os
import requests
from bs4 import BeautifulSoup

def get_links(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html5lib")
    print("status_code is ", req.status_code)
    links = []
    for link in soup.select(".view_img_link"):
        link = "http:" + str(link["href"])
        if link.endswith(".jpg"):
            links.append(link)
    return links


def save(url, path, count):
    name = path + str(url)[-34:]
    if os.path.exists(name):
        print(name[-34:] + " has exited.")
        return False
    else:
        req = requests.get(url)
        file = open(name, "wb")
        file.write(req.content)
        file.close()
        print("the {0} picture finished".format(count))
        return True
