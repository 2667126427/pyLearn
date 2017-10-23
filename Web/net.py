# coding: utf-8
import requests

req = requests.get('http://one.hust.edu.cn')
req.encoding = req.apparent_encoding

text = req.text
start = text.find("'") + 1
end = text.find("'", start)
if end == -1:
    exit()
text = text[24:480].strip()
url='http://192.168.50.3:8080/eportal/InterFace.do?method=login'
queryString = text[text.find('?')+1:]
options = {
'userId': 'U201614700',
'password': 'aorz2017',
'service': '',
'operatorPwd': '',
'validcode': '',
'queryString': queryString
}
req = requests.get(url=url, params=options)
req.encoding=req.apparent_encoding
print(req.text)
