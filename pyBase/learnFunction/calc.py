def calc(*args):
    sum = 0
    for x in args:
        sum += x * x
    return sum


# 普通参数 默认参数 可变参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


if __name__ == '__main__':
    nums = [1, 3, 4, 5]
    print(calc(1, 3, 4, 5))
    print(calc(1, 3))
    print(calc(*nums))
