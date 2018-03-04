import json
'''https://pan.baidu.com/s/1jJ2tilw'''
with open('name.json', 'rb') as fp:
    names = json.loads(fp.read())

print(len(names))
for name in names[:10]:
    print(name['id'], ':', name['name'])
