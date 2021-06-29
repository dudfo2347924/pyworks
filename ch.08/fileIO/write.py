# 파일 열기(open())-> 파일쓰기(write())-> 파일 닫기(close())
f = open('C:/pyfile/hello.txt', 'w')
f.write("Hello~ Python")
#f.write('1000')
f.write('\n%d' % 100)
f.write('\n')
num = "%d" % 100000
f.write(num)
f.close()