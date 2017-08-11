import os
import requests


#get the picture link
def get_picture_link(url):
    res = requests.get(url)
    text = res.text
    # just sraech the header
    start_str = "g_img={url: \"/"
    start = text.find(start_str)
    # search the end
    end = text.find("\",id", start)
    result = url + text[start + len(start_str) - 1:end]
    print("Find the url: " + result)
    # return the result
    return result


# save the picture
def save_picture(link):
    res = requests.get(link)
    # transform to a string
    link = str(link)
    # find the start of name
    last = link.rfind("/")
    # get the end index
    _index = link.find("_")
    f_name = link[last + 1: _index] + ".jpg"
    # check if the file has existed
    if os.path.exists(f_name):
        print(f_name + " has existed")
    else:
        # save the file
        fout = open(f_name, "wb")
        fout.write(res.content)
        fout.close()
        print(f_name + " was downloaded successfully")


if __name__ == '__main__':
    # the homepage of bing
    url = "http://www.bing.com"
    link = get_picture_link(url)
    save_picture(link)
