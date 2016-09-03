#  File: Mondrian.py

#  Description: Draws a koch curve

#  Student Name: Nelson Morrow

#  Student UT EID: ntm432

#  Course Name: CS 313E

#  Unique Number:

#  Date Created: 03/05/16

#  Date Last Modified:

#Koch curve.
#start: F
#rules: F -> F+F-F-F+F 1 -> 1 2 1 3 1 3 1 2 1
#This means forward -> forward, left turn, forward, right turn, forward, right turn, forward, left turn, forward
import turtle, math

# draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def distance (x, x1):
    x2 = (x[0] - x1[0]) * (x[0] - x1[0])
    y2 = (x[1] - x1[1]) * (x[1] - x1[1])
    return ((x2 + y2) ** 0.5)

def drawSquare (ttl, x, y, side):
  ttl.penup()
  ttl.goto(x, y)
  ttl.setheading(0)	# set the pen in the +ve x direction
  ttl.pendown()
  for iter in range (4):
    ttl.forward(side)
    ttl.right(90)
  ttl.penup()

# returns the midway between two points
def midpoint (p1, p2):
  p = [0, 0]
  p[0] = (p1[0] + p2[0]) // 2
  p[1] = (p1[1] + p2[1]) // 2
  return p

# draw recursively a snowflake
def snow_flake (ttl, order, p1, F, temp):
    if order == 1:
        angle = 0
        length = float(800)
        divisor = 0
        #(1/(.4**(temp-1)))
        for j in range(len(F[temp])):
            if(F[temp][j]) == 'F':
                divisor = divisor+1
        length = length/divisor
        length = length*((2**(temp-1)))
        length = abs(length-(1/(.89999**(temp-1))))
        ttl.penup()
        ttl.goto (p1[0]+length**(1/(.89999**(temp-1))), p1[1])
        ttl.pendown()
        for k in range(len(F[temp])):
            if(F[temp][k]) == 'F':
                ttl.forward(length)
            if(F[temp][k]) == '+':
                angle = angle+90
                ttl.setheading(angle)
            if(F[temp][k]) == '-':
                angle = angle - 90
                ttl.setheading(angle)
                #k = k+3
    else:
      spot = len(F)-order
      for i in range(len(F[spot])):
          if(F[spot][i]) == 'F':
              #F + F - F - F + F
             F[spot+1]+= ['F']
             F[spot+1]+= ['+']
             F[spot+1]+= ['F']
             F[spot+1]+= ['-']
             F[spot+1]+= ['F']
             F[spot+1]+= ['-']
             F[spot+1]+= ['F']
             F[spot+1]+= ['+']
             F[spot+1]+= ['F']
          if(F[spot][i]) == '+':
              F[spot+1]+= ['+']
          if(F[spot][i]) == '-':
              F[spot+1]+= ['-']
      snow_flake (ttl, order-1, p1, F, temp)

     # if(last % 2 == 0):
    #      upcount = upcount+1


def main():
  # prompt the user to enter an order for the snow flake
  order = int (input ('Enter an order: '))

  # put label on top of page
  turtle.title ('Koch Curve')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()

  # assign a color to the turtle object
  ttl.color ('navy')

  # draw the snow flake
  p1 = [-400, -350]
  order = order+1
  F = [[0 for x in range(1)] for x in range(order)]
  F[0][0] = 'F'

  temp = order-1
  snow_flake (ttl, order, p1, F, temp)
 # snow_flake (ttl, order, p2, p3)
 # snow_flake (ttl, order, p3, p1)
  # persist drawing
  turtle.done()


main()
