import turtle as t

def turn_up():
    t.setheading(90)
    t.forward(10)
'''
def turn_upright():
    t.setheading(45)
    t.forward(10)

def turn_upleft():
    t.setheading(135)
    t.forward(10)

def turn_downright():
    t.setheading(315)
    t.forward(10)

def turn_downleft():
    t.setheading(235)
    t.forward(10)
'''

def turn_down():
    t.setheading(270)
    t.forward(10)

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def clear():
    t.clear()

t.shape("turtle")
#t.onkeypress(turn_upright, "Right+Up")
#t.onkeypress(turn_upleft, "Left+Up")
#t.onkeypress(turn_downright, "Right+Down")
#t.onkeypress(turn_downleft, "Left+Down")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(clear, "Escape")

t.listen()

t.mainloop()