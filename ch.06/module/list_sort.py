#리스트 최대값,최솟값,정렬


score = [70,80,50,60,90,45]
max = score[0]
min = score[0]
n = len(score)
score.sort()
print(score)
'''
for i in range(1, n):
    if max < score[i]:
        max = score[i]
print("최고 점수 : ", max)

for i in range(1, n):
    if min > score[i]:
        min = score[i]
print("최저 점수 : ", min)
'''
for i in range(0,n):
    for j in range(0,n-1):
        if score[j] > score[j+1]:
            score[j],score[j+i] = score[j+1], score[j]
            print(score[j])
        
    
