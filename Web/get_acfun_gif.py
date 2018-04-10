import requests

url = 'http://cdn.aixifan.com/dotnet/20130418/umeditor' \
      '/dialogs/emotion/images/ac/{0}.gif'


def get_pic(index: int):
    r = requests.get(url.format(index))
    if r.status_code != 200:
        return False
    else:
        with open(str(index) + '.gif', 'wb') as fp:
            fp.write(r.content)
        return True


if __name__ == '__main__':
    index = 1
    while get_pic(index):
        print(str(index) + " was downloaded.")
        index += 1
