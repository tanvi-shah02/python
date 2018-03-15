import turtle
def draw_triangle():
    window=turtle.screen()
    window=bgcolor("yellow")
    a=turtle.Turtle()
    a.right(60)
    a.forward(60)
    a.right(60)
    a.forward(60)
    a.right(60)
    a.forward(60)
    window.exitonclick()

draw_trianle()
