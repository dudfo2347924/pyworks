
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

# 3번
