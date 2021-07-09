x = int(input("게시글의 총 건수"))
y = int(input("페이지당 보여주는 글 수"))

def getpage(x,y):
    if x % y == 0:
        return x//y
    else:
        return x//y+1
p = getpage(x,y)
print(p)
'''
def getpage(x,y):
    if x % y == 0:
        page = x//y
    if x % y != 0:
        page = x//y+1
    return page
p = getpage(x,y)

print("게시글 수 : " , x)
print("보여줄 수 : " , y)
print("페이지 수 : " , p)
'''

