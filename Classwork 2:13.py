import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

square(150)
sqaure(200)
square(250)
square(300)

def rectangle(size):
    for i in range(4):

    import turtle as t

def right():
    t.left(90)
    t.left(90)
    t.left(90)

def drawStep():
    t.forward(50)
    t.left(90)
    t.forward(50)
    right()

def drawSide():
    drawStep()
    drawStep()
    drawStep()
    t.forward(50)
    t.right(90)

def drawDiamond():
    drawSide()
    drawSide()
    drawSide()
    drawSide()

drawDiamond()
