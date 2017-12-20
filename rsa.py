p, q = 53, 61
N = p * q
phiN = (p - 1) * (q - 1)
e = 17
d = 2753
message = 29
print('message:', message)
en = message**e % N
print('after encode:', en)
de = en**d % N
print('after decode:', de)
exit(0)
