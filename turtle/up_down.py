#다른곳에 도형 그리기.
import turtle as t

t.shape("turtle")

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.right(360/n)

def polygon2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(5)
polygon2(6,100)

t.up()
t.back(100)
t.right(90)
t.down()

polygon(20)
polygon2(3,200)


'''
for x in range(4):
    
    t.right(90)
    t.forward(100)
'''
