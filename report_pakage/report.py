import requests
from bs4 import BeautifulSoup

header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/" \
         "537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
main_url = "http://huststudy.hustonline.net/{}"


def get_page(_id):
    req = requests.get(main_url.format(_id), header)
    req.encoding = "utf-8"
    print(req.status_code)
    soup = BeautifulSoup(req.text, "html.parser")
    title = soup.select(_id)
    title = title[0].select('h2')[0].text
    i = 1
    # print(soup.select("a"))
    for item in soup.find_all("a"):
        print(item)
        yield title + str(i), item["href"][0]
        i += 1


def get_img(name, url):
    file_name = name + "jpg"
    data = requests.get(url)
    with open(file_name, 'rb') as wr:
        wr.write(data.content)
        wr.close()


def __main__():
    page = "#page{}"
    for i in range(1, 2):
        for name, item in get_page(page.format(i)):
            i += 1
            print(name, item)
            # get_img(name, item)


if __name__ == "__main__":
    __main__()
