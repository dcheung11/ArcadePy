#Damien game 3
#Sapce invaders

import turtle
import os
import math
import random

#Screen and border
window = turtle.Screen()
window.bgcolor("black")
window.title("Damien SPACE INVADERS")
window.bgpic("spacebg.gif")

turtle.register_shape("enemy.gif") #registered my own gifs to the turtle module
turtle.register_shape("player.gif")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600) #angular turn of the pen
    border_pen.lt(90)
border_pen.hideturtle()


#SCORE and its graphics
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,275)
scorestring = "Score %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()



#Make  player graphics
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90) #rotates the triangle "user" so its up facing

playerspeed = 15


number_of_enemies = 5
enemies =[] #list

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

#the bad guy
for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#player projectile
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#the "phases" for the bullet are ready and fire
bulletphase = "ready"

#left right player movement
def go_left():
    x= player.xcor()
    x -= playerspeed #each time this func is called, the traingle will move one "speed" unit left
    if x < -280:
        x = -280
    player.setx(x)
    
def go_right():
    x= player.xcor()
    x += playerspeed #each time this func is called, the traingle will move one "speed" unit left
    if x > 280:
        x = 280
    player.setx(x)

def shoot_bullet():
    global bulletphase
    if bulletphase == "ready":
        bulletphase = "fire"
        x = player.xcor()
        y = player.ycor() +10 
        bullet.setposition(x, y)
        bullet.showturtle()

def collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


turtle.listen()
turtle.onkey(go_left, "Left")
turtle.onkey(go_right, "Right")
turtle.onkey(shoot_bullet, "space")

#main loop
while True:
    
    for enemy in enemies:
        #bad guy movement
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x) #the enemy moves left to right "enemyspeed" pixels/ update time
        
        #back and forth enemy  movement
        if enemy.xcor() > 280:
            #down after side border enemy
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)   
            enemyspeed *= -1 #reverse motion

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1 #reverse motion

        if collision(bullet, enemy):
            bullet.hideturtle()
            bulletphase = "ready"
            bullet.setposition(0,-400)
            x = random.randint(-200,200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

            #updaet score
            score += 100
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))


        if collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break
        
            
# moving projectile
    if bulletphase == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #bullet/top border collision

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletphase = "ready"

    

delay = raw_input("ENTER to Finish")



