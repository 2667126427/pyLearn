from math import sqrt


def sol(a, b, c):
    judge = b * b - 4 * a * c
    if judge < 0:
        return "No answer"
    elif judge == 0:
        x1 = -b - sqrt(judge)
        return x1, x1
    else:
        x1 = -b - sqrt(judge)
        x2 = -b + sqrt(judge)
        return x1, x2

if __name__ == '__main__':
    print(sol(2,3, 1))
