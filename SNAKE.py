#Damien's second game - classic snake arcade game
#november 2019
def run_snake():
    
    import turtle
    import time
    import random


    delay = 0.1

    #score vars
    score = 0
    high_score = 0

    #Setting up a window for this game to run in 
    window = turtle.Screen()
    window.title("Damien Snake")
    window.bgcolor("Green")
    window.setup(width=500, height=500)
    window.tracer(0) #stops in game updating screen

    #Snake start block
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("blue")
    head.penup()
    head.goto(0,0)
    head.direction =  "stop"

    #SNAKE apple
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    snake_body = []

    # pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 210)
    pen.write("Score: 0  High Score: 0", align= "center", font=("Courier",22, "normal"))


    #functions
    #directions
    def turn_up():
        if head.direction != "down":
            head.direction = "up"

    def turn_down():
        if head.direction != "up":
            head.direction = "down"

    def turn_right():
        if head.direction != "left":
            head.direction = "right"

    def turn_left():
        if head.direction != "right":
            head.direction = "left" 

    #continious movement
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y+20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y-20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x+20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x-20)
    a=1
    if a == 1:
            
        #Keyboard attach
        window.listen()
        window.onkeypress(turn_up, "Up")
        window.onkeypress(turn_down, "Down")
        window.onkeypress(turn_left, "Left")
        window.onkeypress(turn_right, "Right")


        #MAIN
        while True:
            window.update()

            #snake head X border collision
            if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                #get rid of segments
                for segment in snake_body:
                    segment.goto(1000,1000)

                #snake body list (reset)
                snake_body.clear()

                #score reset
                score = 0
                
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("Courier", 22, "normal"))

            if head.distance(food) < 20: #snake head hits food
                any_square_x = random.randint(-240,240) #moving the food after eaten
                any_square_y = random.randint(-240,240)
                food.goto(any_square_x, any_square_y)

                #add segment to snake
                new_snake_body = turtle.Turtle()
                new_snake_body.speed(0)
                new_snake_body.shape("circle")
                new_snake_body.color("skyblue")
                new_snake_body.penup()
                snake_body.append(new_snake_body)

                #shortened delay
                delay -= 0.001

                #add score
                score += 10
                
                if score > high_score:
                     high_score= score

                pen.clear() 
                pen.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("Courier", 22, "normal"))

            #complex code for the segments moving in reverse order
            for index in range(len(snake_body)-1, 0,-1):
                x = snake_body[index-1].xcor()
                y = snake_body[index-1].ycor()
                snake_body[index].goto(x,y)

            #new segments follow the snake head
            if len(snake_body) > 0:
                x = head.xcor()
                y = head.ycor()
                snake_body[0].goto(x,y)

            move()

            #Head / body segment collisions
            for segment in snake_body:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"

            #get rid of segments
                    for segment in snake_body:
                        segment.goto(1000,1000)

                    #snake body list
                    snake_body.clear()

                    #reset delay
                    delay = 0.1
                    
                    pen.clear()
                    pen.write("Score: {}  High Score: {}".format(score,high_score), align="center", font=("Courier", 22, "normal"))

            time.sleep(delay)


        window.mainloop


