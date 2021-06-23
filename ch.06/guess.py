#숫자 추측 게임

import random

com = random.randint(1,30)
i=0

while True:
    guess = int(input("맞혀보세요.(1~30) : "))
    
    if i > 5:
        print("실패하셧습니다.")
        break
    elif com == guess:
        print("정답입니다.")
        break
    elif com < guess:
        i += 1
        print("너무 큼니다.",i)
    elif com > guess:
        i += 1
        print("너무 작습니다.",i)

