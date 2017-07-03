from functools import reduce


def str2float(s):
    # s = ''
    if '.' in s:
        zh, xi = s.split('.')
        return str2int(zh) + str2dot(xi)
    else:
        return str2int(s)


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def str2dot(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s)) / 10 ** len(s)


if __name__ == '__main__':
    print(str2float("123"))
