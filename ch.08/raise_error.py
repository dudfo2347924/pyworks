class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("독수리가 하늘 높이 난다.")

eagle = Eagle()
eagle.fly()