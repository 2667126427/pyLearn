import sys


def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon

print("0.11 = 0.11 * 2 / 2 ?", equal_float(0.11, 0.11 * 2 / 2))
