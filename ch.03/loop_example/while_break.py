#while - break - 반목 조건문
'''
i=1
while True:
    print(i)
    i += 1
    if i>10:
        break
'''
i = 1

while True:
    print(i)
    i += 1
    if i>10:
        print("반복을 계속 할까요?[y/n] : " )
        i=1
        answer = input()

        if answer == 'y':
            print("반복을 계속 한다")
        elif answer == 'n':
            print("반복을 중단 한다")
            break
        else:
            print("잘못된 입력입니다.")
