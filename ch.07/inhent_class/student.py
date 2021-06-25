from person import  Person

# student 클래스 - 학번(stuld)

class Student(Person):
    def __init__(self, name, age, stuid):
        super().__init__(name, age)
        self.stuid = stuid

    def showinfo(self):
        print(self.name, self.age, self.stuid)


s1 = Student("이강",19,101)
s1.showinfo()
s2 = Student("막강",17,201)
s2.showinfo()