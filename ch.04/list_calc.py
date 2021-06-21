#리스트의 연산

score = [70,80,50,60,90,40]
sum = 0
count = len(score)

#합계
for i in score:
    sum += i
    print("i = %d, sum = %d " % (i,sum))

#평균
평균 = sum/count
    
          
print ( "개수 : %d개" % count)
print ( "합계 : %d개" % sum)
print ( "평균 : %.f개" % 평균)
