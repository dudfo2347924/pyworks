'''
# 1, 2번
class Calculater:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculater(Calculater):
    def minus(self, val):
        self.value -= val
        return self.value


class MaxLimitCalculater(UpgradeCalculater):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

        return self.value


cal0 = Calculater()
cal0.add(10)
print(cal0.value)

cal1 = UpgradeCalculater()
cal1.add(10)
cal1.minus(7)
print(cal1.value)


cal2 = MaxLimitCalculater()
cal2.add(100)
cal2.add(130)
print(cal2.value)

cal3 = MaxLimitCalculater()
cal3.add(100)
cal3.minus(100)
cal3.add(130)
print(cal3.value)
# 4번

li = [1,-2,3,-5,8,-3]

print(list(filter(lambda x : x >=0,li)))

def list(x):
    x2=[]
    for i in x:
        if i >= 0:
            x2.append(i)
    return x2

li = [1,-2,3,-5,8,-3]
li2 = list(li)


print(li2)

# 6번
def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2

li = [1,2,3,4]
li2 = times(li)
print(li2)
print(list(map(lambda x: x * 3,li)))

# 7번
def find_max(li):
    max = li[0]

    n = len(li)
    for i in range(n):
        if max < li[i]:
            max= li[i]

    return max

d1 = [-8, 2, 7, 5, -3, 5, 0, 1]

max2 = find_max(d1)

print(max2)
max = max(d1)
min = min(d1)
print(max)
print(min)
print(max+min)
'''

# 9번







