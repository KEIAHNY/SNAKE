from turtle import Turtle, Screen
import time
import random 
import turtle

#Proměnné
score = 0
highest_score = 0
speed = 0.1

screen = turtle.Screen()
screen.register_shape("grass.gif")

screen.title("SNAKE GAME")
screen.bgcolor("black")
screen.setup(width =600,height=600)
screen.tracer(False) #zamrznutí stránky - neobnovuje se 

canvas = turtle.Turtle()
canvas.shape("grass.gif")
canvas.goto(0,-25)
canvas.speed(0)

#HADÍ HLAVA, JABKO, ČÁSTI TĚLA
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)

body_parts = []

#NÁPISY
score_sign = Turtle("square")
score_sign.speed(0) #nehýbe se to 
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0,262)
score_sign.write("Skóre: 0 Nejvyšší skóre: 0", align="center", font=("Verdana", 15))

line = Turtle()
line.hideturtle()
line.penup()
line.goto(-300,250)
line.pendown()
line.pencolor("white")
line.pensize(2)
line.forward(600)
line.speed(10)


#FUKCE
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"


#KLIKNUTÍ NA KLÁVESY
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")


#HLAVNÍ CYKLUS
while True:
    screen.update()

    #kontrola kolize s hranou obrazovky
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 220 or head.ycor() < -290: 
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #skryjeme části těla
        for one_body_part in body_parts:
            one_body_part.goto(1500,1500)
        #vyprázdníme list s částmi těla
        body_parts.clear() #bez tohoto by se zase vrátili za hlavou

        #resetování skóre
        score = 0
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Verdana", 15))

        #resetování rychlosti
        speed = 0.1

    #kolize hlavy s jablkem
    if head.distance(apple) < 20: #KOLIZE
        apple.goto(random.randint(-280,280), random.randint(-280,220))

        new_body_part  = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)
    
        #zvýšení skóre
        score += 1 
        if score  > highest_score:
            highest_score = score

        #zvýšení rychlosti
        speed -=0.01

        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Verdana", 15))


    for i in range(len(body_parts)-1, 0, -1):
        x = body_parts[i-1].xcor()
        y = body_parts[i-1].ycor()
        body_parts[i].goto(x,y)


    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)

#dám na pozici hlavy a hned se hlava pohne
    move()

    # Hlava narazila do těla
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #skryjeme části těla
            for one_body_part in body_parts:
                one_body_part.goto(1500,1500)
            #vyprázdníme list s částmi těla
            body_parts.clear() #bez tohoto by se zase vrátili za hlavou

            #resetování skóre
            score = 0
            score_sign.clear()
            score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Verdana", 15))

            #resetování rychlosti
            speed = 0.1


    time.sleep(speed)

