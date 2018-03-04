import json

arr = []
no = 0
with open('hobbies.txt', 'r') as fp:
    for name in fp.readlines():
        arr.append({'no': no, 'hobby': name.strip()})
        no += 1
json_obj = json.dumps(arr)
with open('hobbies.json', 'w') as fp:
    fp.write(json_obj)
print("generate hobbies done.")
