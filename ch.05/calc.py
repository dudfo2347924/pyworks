#return이 있는 함수

def 덧셈(x,y):
    return x + y

def 뺄셈(x,y):
    return x - y

def 곱셈(x,y):
    return x * y

def 나눔(x,y):
    return x / y
x = int(input('숫자를 입력하세요 : '))
y = int(input('숫자를 입력하세요 : '))

합 = 덧셈(x,y)
차 = 뺄셈(x,y)
곱 = 곱셈(x,y)
나눔 = 나눔(x,y)
print(합,차,곱,나눔)
