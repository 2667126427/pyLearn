import hashlib

str = 'I am a string.'
hash_md5 = hashlib.md5(str.encode('utf-8'))

print(hash_md5.hexdigest())
