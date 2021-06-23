#도형 그리기

import turtle as t

t.shape("turtle")

n = 5
for i in range(n):
    t.forward(100)
    t.right(360/n)

t.color('red')
t.pensize(4)
n=8

for i in range(0,n):
    t.forward(100)
    t.right(360/n)

t.color('blue')
t.pensize(2)

t.circle(100)

