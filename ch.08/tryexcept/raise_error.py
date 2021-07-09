class Bird:
    def fly(self):
        print("새가 날아감니다.")
        raise NotImplementedError
0
class Eagle(Bird):
    def fly(self):
        print("독수리가 하늘 높이 난다.")

eagle = Eagle()
eagle.fly()