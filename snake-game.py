import turtle
import time
import random


delay = 0.1
score = 0


wn = turtle.Screen()
wn.title('Snake Game made by amir')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'



food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)


segments = []



def go_up():
        head.direction = 'up'


def go_down():
        head.direction = 'down'

def go_left():
        head.direction = 'left'

def go_right():
        head.direction = 'right'




def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)


wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_right, 'd')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_down, 's')


while True:
    wn.update()


    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0,0)
        head.direction = 'stop'

        
        for segment in segments:
            segment.goto(1000,1000)

        
        segments.clear()
        score = 0
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)


  
    if head.distance(food) < 20:
 
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)



        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('yellow')
        new_segment.penup()
        segments.append(new_segment)
        score = score+10
        print(score)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move the segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)




    move()

    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(0,0)
            head.direction = 'stop'


            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            score = 0
            x = random.randint(-290,290)
            y = random.randint(-290,290)
            food.goto(x,y)




    time.sleep(delay)


wn.mainloop()
