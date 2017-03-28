fibo = [0, 1, 1];
t = fibo[2]
i = 3
while t < 2**32:
    fibo += [fibo[i - 1] + fibo[i - 2]]
    t = fibo[i]
    i += 1

i = 1
for t in fibo:
    if i % 6 == 0:
        print('\n')
    print(str(t))
    i += 1
print(str(i))
print(len(str(t)))
