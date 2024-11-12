import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle object
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed for smooth drawing
pen.width(2)
pen.hideturtle()

# Function to draw a petal
def draw_petal(radius, angle):
    for _ in range(2):
        pen.circle(radius, angle)  # Draw arc (half of the petal)
        pen.left(180 - angle)  # Create symmetry by turning the turtle

# Function to draw a layered flower with a spiral center
def draw_flower_with_spiral():
    num_layers = 12  # Number of layers of petals
    h = 0  # Initial hue for color
    
    # Draw the flower petals in layers
    for layer in range(num_layers):
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.setheading(layer * 30)  # Rotate for each layer
        
        # Change the radius of petals for each layer
        radius = 100 + layer * 10
        angle = 60
        
        # Set the color for each layer
        color = colorsys.hsv_to_rgb(h, 1, 1)
        pen.pencolor(color)
        h += 0.08  # Increment hue to transition smoothly
        
        # Draw multiple petals in a circular pattern
        for _ in range(6):
            draw_petal(radius, angle)
            pen.right(360 / 6)  # Rotate to position for the next petal

    # Move to the center to draw a swirl
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(0)
    
    # Draw a smooth spiral at the center
    h = 0  # Reset hue for color transitions in the swirl
    for i in range(100):
        color = colorsys.hsv_to_rgb(h, 1, 1)
        pen.pencolor(color)
        h += 0.005  # Gradually change hue
        pen.forward(i * 2)  # Increase step length to expand the spiral
        pen.left(59)  # Angle to create the spiral

# Start drawing the layered flower with spiral
draw_flower_with_spiral()

# Complete the drawing
turtle.done()
