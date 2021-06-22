#리스트를 매개 변수로 지정하기
#정수의 평균 계산하기

def avg(a):
    sum=0
    c = len(a)
    for i in a:
        sum += i
        print( 'i = %d , sum = %d' %(i,sum))

    avge = sum/c
    print('학생 수 : ', c)
    return avge

avg = avg([70 , 80 , 60 , 90 , 100])
print("평균 점수 : " , avg)
