import turtle

def draw_circle(x, y, r):
    turtle.penup()
    turtle.goto((x, y))
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    turtle.goto((x, y - r))
    turtle.pendown()
    turtle.circle(r)


turtle.shape('turtle')
draw_circle(0, 0, 50)
draw_circle(200, 200, 100)
draw_circle(100, -100, 50)
