import decimal
import math

a = decimal.Decimal(9876)  # 整数才可以直接赋值
b = decimal.Decimal("54321.012345678987654321")  # 不要直接输入浮点数，这个decimal可以精确表示数字，字符串才行。
print(a + b)
a.exp()
