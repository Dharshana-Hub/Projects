import turtle

Score_A = 0
Score_B = 0
Game_Over = False
'''Display Screen'''
Win = turtle.Screen()
Win.setup(800,600)
Win.bgcolor("Black")
Win.title("PONG GAME")
Win.tracer(0)

def Reset_Game():
    global Score_A, Score_B, Game_Over
    Score_A = 0
    Score_B = 0
    Game_Over = False
    Sc.clear()
    Sc.write("Player A : {}    Player B : {}".format(Score_A, Score_B))
    Ball.goto(0, 0)
    Ball.dx = 0.1
    Ball.dy = 0.1



'''Left Paddle'''
Left_Paddle = turtle.Turtle()
Left_Paddle.speed(0)
Left_Paddle.shape("square")
Left_Paddle.color("White")
Left_Paddle.shapesize(stretch_wid=5,stretch_len=1)
Left_Paddle.penup()
Left_Paddle.goto(-380, 0)

'''Right Paddle'''
Right_Paddle = turtle.Turtle()
Right_Paddle.speed(0)
Right_Paddle.shape("square")
Right_Paddle.color("White")
Right_Paddle.shapesize(stretch_wid=5,stretch_len=1)
Right_Paddle.penup()
Right_Paddle.goto(380, 0)

'''Ball'''
Ball = turtle.Turtle()
Ball.speed(0)
Ball.goto(0,0)
Ball.shape("circle")
Ball.color("Blue")
Ball.penup()
Ball.dx = 0.1
Ball.dy = 0.1

'''Moving Paddles'''
def Left_Paddle_Up():
    if not Game_Over:
        Left_Paddle.sety(Left_Paddle.ycor() + 20)

def Left_Paddle_Down():
    if not Game_Over:
        Left_Paddle.sety(Left_Paddle.ycor() - 20)

def Right_Paddle_Up():
    if not Game_Over:
        Right_Paddle.sety(Right_Paddle.ycor() + 20)

def Right_Paddle_Down():
    if not Game_Over:
        Right_Paddle.sety(Right_Paddle.ycor() - 20)

def Ask_To_Play_Again():
    while True:
        Answer = Win.textinput("Play Again?", "Press Y to play again, N to quit: ").lower()
        if Answer == 'y':
            Reset_Game()
            break
        elif Answer == 'n':
            Win.bye()
            break

def Quit_Game():
    global Game_Over
    Game_Over = True
    Sc.clear()
    Sc.write("Game Quit! Press Y to play again, N to quit", align="center", font=("Calibri", 24, "bold"))
    Ask_To_Play_Again()
    


Win.listen()
Win.onkeypress(Left_Paddle_Up, 'w')
Win.onkeypress(Left_Paddle_Down, 's')
Win.onkeypress(Right_Paddle_Up, 'Up')
Win.onkeypress(Right_Paddle_Down, 'Down')
Win.onkeypress(Quit_Game, 'q')

'''Score'''
Sc = turtle.Turtle()
Sc.speed(0)
Sc.color("white")
Sc.hideturtle()
Sc.penup()
Sc.goto(0, 260)
Sc.write("Player A : 0    Player B : 0", align = "center", font = ("Calibri", 24, "bold"))

def Check_Winner():
    global Game_Over
    if Score_A == 5 and Score_B == 5:
        Sc.clear()
        Sc.write("Game Draw! Press Y to play again, N to quit", align="center", font=("Calibri", 24, "bold"))
        Game_Over = True
        Ask_To_Play_Again()

    elif Score_A == 5:
        Sc.clear()
        Sc.write("Player A Wins! Press Y to play again, N to quit", align="center", font=("Calibri", 24, "bold"))
        Game_Over = True
        Ask_To_Play_Again()

    elif Score_B == 5:
        Sc.clear()
        Sc.write("Player B Wins! Press Y to play again, N to quit", align="center", font=("Calibri", 24, "bold"))
        Game_Over = True
        Ask_To_Play_Again()


while True:
    Win.update()
    '''Ball Movement'''
    if not Game_Over:
        Ball.setx(Ball.xcor() + Ball.dx)
        Ball.sety(Ball.ycor() + Ball.dy)

        '''Ball - Wall Collision'''
        if Ball.ycor() > 290:
            Ball.sety(290)
            Ball.dy *= -1
        if Ball.ycor() < -290:
            Ball.sety(-290)
            Ball.dy *= -1

        '''Right Wall'''
        if Ball.xcor() > 390:
            Ball.setx(390)
            Ball.dx *= -1
            Score_A += 1
            Sc.clear()
            Sc.write("Player A : {}    Player B : {}".format(Score_A, Score_B), align="center", font=("Calibri", 24, "bold"))
            Check_Winner()

        '''Left Wall'''
        if Ball.xcor() < -390:
            Ball.setx(-390)
            Ball.dx *= -1
            Score_B += 1
            Sc.clear()
            Sc.write("Player A : {}    Player B : {}".format(Score_A, Score_B), align="center", font=("Calibri", 24, "bold"))
            Check_Winner()

        '''Ball - Paddles Collision'''
        if Ball.xcor() > 370 and Ball.ycor() < Right_Paddle.ycor() + 50 and Ball.ycor() > Right_Paddle.ycor() - 50:
            Ball.setx(360)
            Ball.dx *= -1
        if Ball.xcor() < -370 and Ball.ycor() < Left_Paddle.ycor() + 50 and Ball.ycor() > Left_Paddle.ycor() - 50:
            Ball.setx(-360)
            Ball.dx *= -1

