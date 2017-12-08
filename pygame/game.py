"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
import math
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)


def draw_rock(screen,x,y):
    pygame.draw.ellipse(screen,BLACK,[x,y,5,5],0)
    
def draw_snitch(screen,x,y):
    pygame.draw.ellipse(screen,RED,[x,y,5,5],0)

# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
x = 700
y= 500
x2 = 300
y2 = 400

sx = 400
sy = 200

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -2
            elif event.key == pygame.K_RIGHT:
                x_speed = 2
            elif event.key == pygame.K_UP:
                y_speed = -2
            elif event.key == pygame.K_DOWN:
                y_speed = 2
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    x2 = x2 + .02 * (x_coord - x2)
    y2 = y2 + .02*(y_coord-y2)
    delx = .01 * (x_coord - x)
    dely = .01*(y_coord-y)
    x = x + delx 
    y = y + dely 
    
    sx = sx +  random.randint(0,15) * random.randint(-1,1) + .003*(sx-x_coord)
    sy = sy + random.randint(0,15) * random.randint(-1,1) + .003*(sy-y_coord)
    if math.sqrt( ((x-x_coord)**2) + ((y-y_coord)**2)) <= 6 or math.sqrt( ((x2-x_coord)**2) + ((y2-y_coord)**2)) <=6:
        done = True
    # --- Drawing Code
    if math.sqrt( ((sx-x_coord)**2) + ((sy-y_coord)**2)) <= 12:
        done = True
    
    if sx > 700:
        sx = 700
    if sy > 500:
        sy = 500
    if sy < 0:
        sy = 0
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    draw_stick_figure(screen, x_coord, y_coord)
    draw_rock(screen,x,y)
    draw_rock(screen,x2,y2)
    draw_snitch(screen,sx,sy)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.

pygame.quit()
