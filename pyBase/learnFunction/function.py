def add(x, y, f):
    return f(x) + f(y)

if __name__ == '__main__':
    print(add(-5,6,abs))