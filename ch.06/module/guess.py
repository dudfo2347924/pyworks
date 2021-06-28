#숫자 추측 게임

import random

com = random.randint(1,30)
i=0

while True:
    try:
        i += 1
        guess = int(input("맞혀보세요.(1~30) : "))

        if i > 5 and com == guess :
            print("정답입니다.")
            break
        elif com == guess:
            print("정답입니다.")
            break
        elif i > 5 and com != guess :
            print("실패하셧습니다.")
            break
        elif com < guess:
            print("너무 큼니다.",i,"번 틀리셧습니다.")
        elif com > guess:
            print("너무 작습니다.",i,"번 틀리셧습니다.")
        elif 30 < guess or guess < 1:
            i -= 1
            print("1~30의 숫자를 입력하세요.")
    except ValueError:
        i -=1
        print("숫자가 아님니다. 다시 입력해주세요.")

