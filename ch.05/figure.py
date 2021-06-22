#도형의 면적을 계산하는 함수 정의와 사용

w = int(input('너비를 입력하세요. : '))
h = int(input('높이를 입력하세요. : '))

def square(w,h):
    area = w*h
    return area

print('사각형의 면적 : ',square(w,h))

def triangle(w,h):
    area = w*h/2
    return area

print('삼각형의 면적 : ',triangle(w,h))
