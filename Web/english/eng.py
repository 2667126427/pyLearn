import requests
from bs4 import BeautifulSoup as Soup


def save_audio(link):
    """
    open the link and save the mp3 file
    """
    req = requests.get(link)
    req.raise_for_status()
    req.encoding = req.apparent_encoding
    soup = Soup(req.text, 'html.parser')
    title = soup.find('h1').text + '.mp3'
    title = title[title.find('第'):]
    src = 'http://www.tingliku.com' + soup.find('audio')['src']
    src_req = requests.get(src)
    with open(title, 'wb') as file:
        file.write(src_req.content)


def main():
    """
    main function
    start the thread
    """
    start = 2605
    end = 2634
    url = 'http://www.tingliku.com/tingli/ielts_story/{0}.html'
    for i in range(start, end + 1):
        save_audio(url.format(i))


if __name__ == '__main__':
    main()
    