import re

string = 'helllllo world what'
pattern = re.compile('he(.*?)o')
res = pattern.match(string)
print(res.group(1))

print(str(1000).zfill(2))