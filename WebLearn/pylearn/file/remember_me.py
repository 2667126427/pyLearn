import json

user_name = input("What is your name: ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(user_name, f_obj)
    print("We'll remember you when you come back, " + user_name + "!")
