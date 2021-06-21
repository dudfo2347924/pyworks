#리스트의 합격 판정
#점수가 60점이상이면 합격 아니면 불합격.

score = [70,80,50,60,90,40]

index=0
'''
for i in score:
    index += 1
    if i > 60:
        print("%d번 학생 %d점 합격" % (index,i) )
    else:
        print("%d번 학생 %d점 불합격" % (index,i) )
'''
n = len(score)
for i in range(0,n):
    if score[i] > 60:
        print("%d번 학생 %d점 합격" % (i+1,score[i]) )
    else:
        print("%d번 학생 %d점 불합격" % (i+1,score[i]) )
