# 파일에 구구단 쓰기

with open('99.txt','w') as f:
    for i in range(2,10):
        for j in range(1,10):
            gugudna = "%d x %d = %d" % (i, j, i * j)
            f.write(gugudna)
            f.write('\n')
        f.write('\n')

with open('99.txt','r') as f:
    data = f.read()
    print(data)