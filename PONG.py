#Damien's game coding, simple pong arcade game with functional collisions, score system, sound effects
#November 2019

import turtle

def run_pong():
    #Creating a WINDOW
    window = turtle.Screen()
    window.title("Damien Pong")
    window.bgcolor("black") #background colour
    window.setup(width=800, height= 600) #dimensions
    window.tracer(0) #prevents the window from updating constantly

    #score variables
    score_1 = 0
    score_2 = 0

    #First Paddle
    paddle_1 = turtle.Turtle()
    paddle_1.speed(0)
    paddle_1.shape("square")
    paddle_1.color("white")
    paddle_1.shapesize(stretch_wid=5, stretch_len = 1) #make the paddle shape
    paddle_1.penup()
    paddle_1.goto(-350,0) #coordinates (left side)

    #Second paddle
    paddle_2 = turtle.Turtle()
    paddle_2.speed(0)
    paddle_2.shape("square")
    paddle_2.color("white")
    paddle_2.shapesize(stretch_wid=5, stretch_len = 1)
    paddle_2.penup()
    paddle_2.goto(350,0) #right side

        #BALL
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0,0) #begins in the middle
    ball.dx = 8 #ball speed (varies by computer system
    ball.dy = 8


        # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260) #scoreboard at top of screen
    pen.write("Player 1: {}  Player 2: {}".format( score_1, score_2), align="center", font=("Courier", 24, "normal"))
                

        # Functions, self explanatory: one "paddle up/ paddle down is worth 20 coordinates
    def paddle_1_up(): 
        y = paddle_1.ycor()
        y += 20
        paddle_1.sety(y)

    def paddle_1_down():
        y = paddle_1.ycor()
        y -= 20
        paddle_1.sety(y)

    def paddle_2_up():
        y = paddle_2.ycor()
        y += 20
        paddle_2.sety(y)

    def paddle_2_down():
        y = paddle_2.ycor()
        y -= 20
        paddle_2.sety(y)

    a=1    

    if a == 1:

        # Keyboard bindings
        window.listen() #call the said command when the binded keyboard button is pressed
        window.onkeypress(paddle_1_up, "w")
        window.onkeypress(paddle_1_down, "s")
        window.onkeypress(paddle_2_up, "Up")
        window.onkeypress(paddle_2_down, "Down")

        #Main
        while True:
            window.update()

            #ball movement
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Border checking
            if ball.ycor() > 290: #if the ball touched the top border..
                ball.sety(290) 
                ball.dy *= -1 #the direction is reversed
                    

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1

            if ball.xcor() > 390: #if the ball touches the left/right border...
                ball.goto(0, 0) #the ball is reset to the middle
                ball.dx *= -1 #reversed direction
                score_1 += 1
                pen.clear()
                pen.write("Player 1: {}  Player 2: {}".format( score_1, score_2), align="center", font=("Courier", 24, "normal"))
                    

            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball.dx *= -1
                score_2 += 1
                pen.clear()
                pen.write("Player 1: {}  Player 2: {}".format( score_1, score_2), align="center", font=("Courier", 24, "normal"))
                    
            if score_1 ==10 or score_2 == 10:
                if score_1 == 10:
                    winner = "Player 1"
                if score_2 == 10:
                    winner = "Player 2"
                pen.speed(0)
                pen.shape("square")
                pen.color("Green")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 0) #middle
                pen.write("GAME OVER! {} WINS!".format(winner), align="center", font=("Courier", 36,"normal"))
                exit()
                    

            #Paddle collision mechanics
            if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
                ball.setx(340) #if the ball is within the dimensions of the paddle
                ball.dx *= -1 #it reverses direction
                
            if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
                ball.setx(-340)
                ball.dx *= -1
