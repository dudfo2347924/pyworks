# with ~as 구문은 f.close()를 생략한다
with open("data.txt","w")as f:
    f.write("안녕하세요.\n")
    f.write("%d\n" % 15000)
    unit = "1 inch = %.2fcm" % 2.54
    f.write(unit)

with open("data.txt","r")as f:
    data = f.read()
    print(data)