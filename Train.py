import turtle
import math
from turtle import *
def drawSquare (ttl, x, y, width, height):
  ttl.penup()
  ttl.goto((x-width/2), (y+height/2))
  ttl.setheading(0)	# set the pen in the +ve x direction
  ttl.pendown()
  for iter in range (2):
    ttl.forward(width)
    ttl.right(90)
    ttl.forward(height)
    ttl.right(90)
  ttl.penup()
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def drawPolygon (ttl, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  for iter in range (num_side):
    ttl.forward (sideLen)
    ttl.left (angle)

def drawWheels(ttl, x, y, num_side, radius):
    sideLen = 2 * radius * math.sin (math.pi / num_side)
    angle = 360 / num_side
    ttl.penup()
    ttl.goto (x, (y-radius))
    ttl.pendown()
    ttl.fillcolor('white')
    ttl.begin_fill()
    for iter in range (num_side):
        if ttl.ycor() > 50:
            ttl.pencolor('blue')
        if ttl.ycor() < 50:
            ttl.pencolor('white')
        ttl.forward (sideLen)
        ttl.left (angle)
    ttl.end_fill()
    ttl.penup()
    radius = .75*radius
    ttl.goto (x, (y-radius))
    ttl.pendown()
    ttl.pencolor('blue')
    ttl.fillcolor('blue')
    ttl.begin_fill()
    sideLen = 2* radius * math.sin (math.pi / num_side)
    for iter in range (num_side):
        ttl.forward (sideLen)
        ttl.left (angle)
    ttl.end_fill()
    ttl.penup()
    radius=(1.3333*radius)
    radius = .6*radius
    ttl.goto (x, (y-radius))
    ttl.pendown()
    ttl.fillcolor('white')
    ttl.begin_fill()
    sideLen = 2* radius * math.sin (math.pi / num_side)
    for iter in range (num_side):
        ttl.forward (sideLen)
        ttl.left (angle)
    ttl.penup()
    ttl.end_fill()
    ttl.pencolor('blue')
    radius = (1/.6) * radius
    radius = .25*radius
    ttl.goto (x, (y-radius))
    ttl.pendown()
    sideLen = 2* radius * math.sin (math.pi / num_side)
    for iter in range (num_side):
        ttl.forward (sideLen)
        ttl.left (angle)
    ttl.penup()

def main():
  # put label on top of page
  turtle.title ('Train')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.pencolor ('blue')
  ttl.fillcolor('black')
  ttl.begin_fill()
  drawSquare (ttl, -70, 90,180, 80)
  ttl.end_fill()
  ttl.fillcolor('black')
  ttl.begin_fill()
  drawSquare (ttl, -200, 100,82, 100)
  ttl.end_fill()
  ttl.fillcolor('black')
  ttl.begin_fill()
  drawSquare (ttl, -200, 153,100, 6)
  ttl.end_fill()
  ttl.fillcolor('grey')
  ttl.begin_fill()
  drawSquare (ttl, -180, 130, 26, 26)
  ttl.end_fill()
  ttl.fillcolor('grey')
  ttl.begin_fill()
  drawSquare (ttl, -220, 130, 26, 26)
  ttl.end_fill()
  drawWheels(ttl,-200, 50,60,30)
  ttl.pencolor ('blue')
  drawWheels(ttl,-104, 50,60,30)
  drawWheels(ttl,-35, 50,60,30)
  ttl.fillcolor('white')
  ttl.begin_fill()
  drawSquare (ttl, -70, 135,30, 10)
  ttl.end_fill()
  ttl.fillcolor('black')
  ttl.begin_fill()
  drawSquare (ttl, -70, 143,10, 6)
  ttl.end_fill()
  ttl.fillcolor('grey')
  ttl.begin_fill()
  drawPolygon(ttl,-40,130,3,20)
  ttl.end_fill()
  ttl.fillcolor('blue')
  ttl.begin_fill()
  drawLine(ttl,20,61,40,61)
  drawLine(ttl,40,61,55,36)
  drawLine(ttl,55,36,20,36)
  drawLine(ttl,20,36,20,61)
  ttl.end_fill()
  ttl.fillcolor('white')
  ttl.begin_fill()
  drawSquare(ttl,27,90,14,55)
  ttl.end_fill()
  ttl.fillcolor('black')
  ttl.begin_fill()
  drawSquare(ttl,37,90,6,22)
  ttl.end_fill()


  # persist drawing
  turtle.done()

main()
