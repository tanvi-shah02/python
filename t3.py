import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")
    a=turtle.Turtle()
    #window.exitonclick
    a.color("green")
    a.forward(100)
    a.right(90)
    a.forward(100)
    a.right(90)
    window.exitonclick()

draw_square()