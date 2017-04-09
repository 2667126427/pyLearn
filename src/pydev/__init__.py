import requests
from bs4 import BeautifulSoup

def __main__():
    i = 0
    if i is 0:
        print("JJJJ")
        
if __name__ == "__main__":
    __main__()
    req = requests.get("https://www.baidu.com")
    req.encoding = "utf-8"
    soup = BeautifulSoup(req.text, "html.parser")
    for item in soup.select("a"):
        print(item.text, item["href"])
    