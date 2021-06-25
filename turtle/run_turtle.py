import turtle as t
import random as r


def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def turn_right():
    t.setheading(0)

def turn_left():
    t.setheading(180)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",15))
    t.home()

def play():
    global score
    global playing

    t.forward(10)
    #빨간 거북이 ai 점수먹으면 속도 증가
    if r.randint(1,10) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5
    te.forward(speed)

    #주인공이 먹이를 먹으면 점수 1 증가
    if t.distance(tf) < 12:
        score += 1
        t.write(score)
        x = r.randint(-230,230)
        y = r.randint(-230,230)
        tf.goto(x, y)

    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over",text)
        playing = False
        t.goto(0,0)
        te.goto(0,200)
        tf.goto(0,-200)
        score = 0


    if playing:
        t.ontimer(play,100)


'''
    if t.distance(tf) >= 12:
        t.ontimer(play, 100)
'''
#메인영역
score = 0
playing = False

t.setup(500,500)
t.title("달려라,거북이")
t.bgcolor('blue')
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

#적 거북이
te = t.Turtle()
te.shape("turtle")
te.color('red')
te.speed(0)
te.up()
te.goto(0,200)

#먹이
tf = t.Turtle()
tf.shape("circle")
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0,-200)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(start, "space")
t.listen()
message("Turtle Game","[space]")

t.mainloop()
