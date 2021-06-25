#학생 클래스 생성과 사용
class Student:
    def __init__(self, 학번, 이름):
        self.학번 = 학번
        self.이름 = 이름

    def get학번(self):
        return self.학번

    def get이름(self):
        return self.이름

s1 = Student(1001,"강산")
print(s1.get학번(),s1.get이름())

s2 = Student(1002,"이산")
print(s2.get학번(),s2.get이름())