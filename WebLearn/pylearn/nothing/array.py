import random


arr = [i**2 for i in range(10)]
random.shuffle(arr)
print(arr)
print(sorted(arr))
print(sorted(arr, reverse=True))
