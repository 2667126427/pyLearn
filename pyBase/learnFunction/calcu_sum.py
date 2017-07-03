def calcu_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


if __name__ == '__main__':
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f)
    print(f())

