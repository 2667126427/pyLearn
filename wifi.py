import requests
import json

url = 'http://one.hust.edu.cn'
r = requests.get(url).text
query = r[r.find('wlanuser'):r.rfind('\'')]
if len(query) > 0:
    user = json.load(open('user_pwd.json', 'r', encoding='utf-8'))
    print('logining...')
    p_url = 'http://192.168.50.3:8080/eportal/InterFace.do?method=login'
    option = {'userId': user['userId'], 'password': user['password'], 'service': '',
              'queryString': query, 'operatorPwd': '', 'validcode': ''}
    post = requests.post(p_url, data=option)
    print(json.loads(str(post.content, 'utf-8'))['result'])
else:
    print('wifi is connected')
    