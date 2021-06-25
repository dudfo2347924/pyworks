# 임의 매개변수가 있는 상속

class  Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name , age, empid):
        super().__init__(name,age)
        self.empid = empid

p1 = Person("한강",25)
print(p1.name, p1.age)

e1 = Employee("다마스커스강",35,201)
print(e1.name, e1.age, e1.empid)