#while문 : "hello"를 10번 반복하기.
'''
i = 1
while i < 11:
    print("Hello~",i)
    i += 1
'''

i = 1
sum = 0

while i < 11:
    sum += i
    #print(i, end = " ")
    print("i = ",i, "sum = ",sum)
    i += 1

#print("합계 : ", sum)
