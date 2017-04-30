#!/usr/bin/env python

# Looking at Shapes
# Project: Making Fractals based on an L system
# Author: Maher Khan 

# importing some libraries that we will need
import turtle
import sys


# some default values
DEFAULT_ANGLE = 90
DEFAULT_LENGTH = 10


# replace every occurence of F in the current string with the axiom
def replace(current, axiom):
    fixed = {'+', '-', '[', ']'}
    
    result = ''
    
    for c in current:
        if c in fixed:
            result += c
            continue
        if c == 'F':
            result += axiom

    return result


# Make the fractal by iterating over the axiom as described in the rule string
def makeFractal(axiom, num=0, rule='F'):

    # Set initator
    result = rule
    for i in xrange(0, num):
        # For ever iteration, translate the rule string
        result = replace(result, axiom)

    return result


# We are going to use turtle to draw the fractal based on the L system
def illustrate(fractal, d=DEFAULT_ANGLE, l=DEFAULT_LENGTH):

    # For tracking turtle positions
    positions  = []

    # Getting our own turtle artist                 
    screen = turtle.Screen()
    artist   = turtle.Turtle()

    screen.bgcolor("black")
    artist.color("white")

    # Don't show the turtle
    artist.hideturtle()  

    # Make the turtle faster
    artist.speed(0)

    # Point up instead of right               
    artist.left(90)               

    # Iterating over the given fractal and drawing it
    for i in xrange(len(fractal)):

        c = fractal[i]

        if c == 'F':
            artist.forward(l)

        if c == 'f':
            artist.penup()
            artist.forward(l)
            artist.pendown()

        if c == '+':
            artist.left(d)

        if c == '-':
            artist.right(d)

        if c == '[':
            positions.append((artist.heading(), artist.pos()))

        if c == ']':
            heading, position = positions.pop()
            artist.penup()
            artist.goto(position)
            artist.setheading(heading)
            artist.pendown()

    # Close the screen if q is pressed
    screen.onkey(screen.bye, 'q')
    screen.listen()
    turtle.mainloop()

#
def render(axiom, rule='F', num_iter=0, angle=DEFAULT_ANGLE, length=DEFAULT_LENGTH):

    fractal = makeFractal(axiom, num_iter, rule)
    illustrate(fractal, angle, length)



if __name__ == '__main__':

    #Examples:

    # Triad clash of quads (by Maher Khan)
    # Axiom: "F+F--F+F+F"
    # Rule: "F-F-F-F"
    # Number of Iterations: 3
    # Angle: 100
    # Length: 50

    # #tiled square (by Maher Khan)
    # Axiom: "F+F--F+F"
    # Rule: "F-F-F-F"
    # Number of Iterations: 3
    # Angle: 90
    # Length: 10
    #
    # (Or, you can just uncomment and run the following code):
    # axiom = "F+F--F+F"
    # fractal = makeFractal(axiom, 3, "F-F-F-F")
    # illustrate(fractal, 90, 10)

    # axiom = "F-F+F+FF-F-F+F"
    # fractal = makeFractal(axiom, 3, "F-F-F-F")
    # illustrate(fractal, 90, 10)

    # #koch curve
    # axiom = "F+F--F+F"
    # fractal = makeFractal(axiom, 3, "F-F-F-F-F-F")
    # illustrate(fractal, 60, 4)

    # axiom = "F[-F]F[+F]F"
    # fractal = makeFractal(axiom, 3, "F")
    # illustrate(fractal, 60, 10)


    axiom = None
    rule = None
    num_iter = None
    angle = None
    length = None

    if(len(sys.argv) == 6):
        axiom = sys.argv[1]
        rule = sys.argv[2]
        num_iter = int(sys.argv[3])
        angle = int(sys.argv[4])
        length = int(sys.argv[5])

        render(axiom, rule, num_iter, angle, length)

    else:
        print("\n")
        print("Welcome to the interactive fractal maker based on an L System...")

        looping = True
        while(looping):
            
            axiom = input("First, what is your Axiom? ")
            rule = input("Second, what is your Rule? ")
            num_iter = input("Third, what is your number of iterations? ")
            angle = input("Fourth, what is your Angle? ")
            length = input("Lastly, what is your Length? ")

            print("Rendering your fractal...")
            render(axiom, rule, num_iter, angle, length)

            looping = input("Do you want to make another fractal? (True/False) ")


