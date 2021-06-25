#Calculater 를 확장한 MoreCalculater 만들기.
from calculator import Calculator

# 제곱수를 계산하는 함수 추가하기
class MoreCalculator(Calculator):
    def pow(self):
        return self.x ** self.y

cal = MoreCalculator(2,3)
print(cal.pow())