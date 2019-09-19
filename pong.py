import turtle

#Ventana
wn = turtle.Screen()
wn.title("El ping pong de Dante")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Jugador A
player_one = turtle.Turtle()
player_one.speed(0)
player_one.shape("square")
player_one.color("white")
player_one.penup()
player_one.goto(-350,0)
player_one.shapesize(stretch_wid=5,stretch_len=1)
count_player_one = 0

#Jugador B
player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape("square")
player_two.color("white")
player_two.penup()
player_two.goto(350,0)
player_two.shapesize(stretch_wid=5,stretch_len=1)
count_player_two = 0

#Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#Linea division
separate = turtle.Turtle()
separate.color("white")
separate.goto(0,400)
separate.goto(0,-400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Jugador A : 0        Juagador B : 0",align="center",font=("Courier",24,"normal"))



def playerA_up():
    y = player_one.ycor()
    y += 20
    player_one.sety(y)


def playerA_dow():
    y = player_one.ycor()
    y -= 20
    player_one.sety(y)

def playerB_up():
    y = player_two.ycor()
    y += 20
    player_two.sety(y)

def playerB_dow():
    y = player_two.ycor()
    y -= 20
    player_two.sety(y)

#teclado
wn.listen()
wn.onkey(playerA_up,"w")
wn.onkey(playerA_dow,"s")

wn.onkey(playerB_up,"Up")
wn.onkey(playerB_dow,"Down")


while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Bordes
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    #bordes derecha y izquierda
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        count_player_one +=1
        pen.clear()
        pen.write("Jugador A : {}        Juagador B : {}".format(count_player_one,count_player_two), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        count_player_two += 1
        pen.clear()
        pen.write("Jugador A : {}        Juagador B : {}".format(count_player_one,count_player_two), align="center", font=("Courier", 24, "normal"))

    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_two.ycor() + 50 and ball.ycor() > player_two.ycor() - 50)):
        ball.dx *=-1

    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_one.ycor() + 50 and ball.ycor() > player_one.ycor() - 50)):
        ball.dx *=-1
