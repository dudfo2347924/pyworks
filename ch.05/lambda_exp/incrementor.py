def incrementor(n):
    return lambda x : x + n

f = incrementor(10)
print(f(2))
print(f(5))
print(f(10))

f = incrementor(20)
print(f(2))
print(f(5))
print(f(10))