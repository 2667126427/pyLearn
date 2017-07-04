# test range function
import random

for i in range(10):  # [0, 10)
    print(i)
print('\n')
for i in range(3, 5):  # [3, 5)
    print(i)
print('\n')
while i is not 3:
    print(i)
    i = random.randint(1, 5)
print('\n')
i = 1
while i < 10:
    print(i)
    i += 1
