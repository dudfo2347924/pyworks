#랜덤하게 걸어가기

import turtle as t
import random as r

t.shape("turtle")
t.speed(0)
t.bgcolor('pink')
t.setup(500,500)

for x in range(1000):
    angle = r.randint(1,360)
    t.setheading(angle)
    t.forward(10)
