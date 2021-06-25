import turtle as t
import random

t.shape('turtle')
t.speed(0)

t.up()
x = random.randint(-230,230)
y = random.randint(-230,230)
t.goto(x,y)



t.mainloop()