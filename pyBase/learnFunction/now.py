#! /usr/
import functools


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


def my_log(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s begin -- %s' % (text, func.__name__))
            fun = func
            print('%s end -- %s' % (text, func.__name__))
            return fun(*args, **kwargs)

        return wrapper

    return decorator


@my_log('log')
def now():
    print('2015-3-25')


@my_log()
def mine():
    print('Hello')


if __name__ == '__main__':
    f = now
    f()
    mine()
