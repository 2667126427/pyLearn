
def fibonacci(N):
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res


if __name__ == "__main__":
    n = input("输入一个数字：")
    res = fibonacci(int(n))
    _len = len(str(res))
    print(_len)
