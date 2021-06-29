#타자 연습 게임
import random as r
import time

f = open('words.txt','r')
word = f.read().split() # 리스트 형태로 가져옴

n = 1
print("[타자게임]준비되면 엔터")
input()

start = time.time()
q = r.choice(word) #랜덤 단어 선택
while n<= 10 :
    print("문제", n, "번")
    print(q)
    x = input()#사용자가 단어를 따라 입력
    if q == x:
        print("통과!")
        n += 1
        q = r.choice(word)
    else:
        print("오타! 다시도전")

print('게임 종료')
end = time.time()
et = end - start
print("타자 시간 : %.2f초" % et)