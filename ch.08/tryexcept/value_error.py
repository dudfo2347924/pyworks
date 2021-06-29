while True:
    try:
        x = int(input("숫자를 입력하세요. : "))
        print(x)
        break
    except ValueError:
        print('잘못 입력하셧습니다.')