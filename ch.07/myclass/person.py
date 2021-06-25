#Person 클래스
class Person:
    def __init__(self):
        self.name = "강하늘"
        self.age = 30

    def getname(self):
        return self.name

    def getage(self):
        return self.age

p = Person() #객체 변수 - 인스턴스(instunce)
print(p.getname(), p.getage())
