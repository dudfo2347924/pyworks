#학생 클래스 생성과 사용
class Student:
    def __init__(self, 학번, 이름):
        self.학번 = 학번
        self.이름 = 이름

    def showinfo(self):
        print(self.학번, self.이름)

if __name__ == "__name__":
    s1 = Student(1001, "박대양")
    s2 = Student(1002, "이산")
    #print(s1.학번, s1.이름)
    s1.showinfo()
    s2.showinfo()
