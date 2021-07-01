
with open('score.txt','r') as f:
    d2 = []
    for i in range(3):
        d2.append(f.readline().split())

    for i in range(3):
        d2[i][1] = int(d2[i][1])
        d2[i][2] = int(d2[i][2])
        add = d2[i][1] + d2[i][2]
        d2[i].append(add)
        d2[i].append(d2[i][3]/2)

    kor_sum = 0
    math_sum = 0

    for i in range(3):
        kor_sum += d2[i][1]
        math_sum += d2[i][2]

#print(d2)

print("   ****** 성적표 ******   ")
print("=========================")
print(" 이름  국어  수학  총점  평균")
print("=========================")
for i in range(3):
    print("  {}    {}   {}   {}    {}".format(d2[i][0], d2[i][1], d2[i][2], d2[i][3], d2[i][4]))
print("=========================")

print("국어 : {}, 수학 : {} ".format(kor_sum/3, math_sum/3))


