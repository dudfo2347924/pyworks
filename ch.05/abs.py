# abs(x)직접 정의
import math

def abs_sign(x):
    if x < 0:
        y = x * -1
        return y
    else:
        return x

n1 = abs_sign(-3)
print(n1)


def abs_square(x):
    y = x * x
    return math.sqrt(y)

n2 = abs_square(-3)
print(n2)
