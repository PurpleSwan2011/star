import turtle
turtle.Screen().bgcolor("orange")
board = turtle.Turtle()

# first triangle of a star
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(150)
board.forward(50)

# second triangle of a star
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
turtle.done()