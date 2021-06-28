# Person 클래스 - 멤버 변수(name,age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    pass

if __name__ == "__main__":
    p1 = Person("한강", 25)
    print(p1.name, p1.age)

    e1 = Employee("다마스커스강", 35)
    print(e1.name, e1.age)

    e1 = Employee("남한강", 45)
    print(e1.name, e1.age)