import turtle

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle() #created an instance of a class called Turtle, we called it brad
    brad.speed(2)
    brad.pen(fillcolor="black", pencolor="blue", pensize=10)
    brad.shape("turtle")

    i = 0
    while (i < 4):
        brad.forward(100)
        brad.right(90)
        i = i + 1
        
    window.exitonclick()


#draw_shape()

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle() #created an instance of a class called Turtle, we called it brad
    brad.speed(10)
    brad.color("yellow")
    brad.shape("turtle")
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_art()
