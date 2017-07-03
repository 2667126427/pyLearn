def squ_sum(x):
    sum = 0
    for i in range(x + 1):
        sum += i * i
    return sum


if __name__ == '__main__':
    x = input("Input a num: ")
    x = int(x)
    print(squ_sum(x))
