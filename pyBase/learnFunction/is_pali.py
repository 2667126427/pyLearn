def is_pali(n):
    a = str(n)
    return a == a[::-1]


if __name__ == '__main__':
    i = input("Input a num:")
    print(is_pali(int(i)))
