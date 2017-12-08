import pygame
import math
import random
from engine import *
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


def draw_bullet(screen,x,y):
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

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
pygame.mixer.music.load('/home/william/toh.wav')
pygame.mixer.music.play()
# Current position
initial = Vector(0,0)
new = Vector(100,100)

jim = Actor(initial,initial,10)
paul = Actor(new,new,10)
actors = [jim,paul]
b = False
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
            elif event.key == pygame.K_w:
                bullet = Actor(Vector(paul.position.x,paul.position.y),initial,5)
                bullet.set_speed(5)
                b = True
                
 
    # --- Game Logic
 
    # Move the object according to the speed vector.
    paul.position.x += x_speed
    paul.position.y += y_speed
    
    
  

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    if b:
        bullet.position.y -= bullet.speed
        draw_bullet(screen,bullet.position.x,bullet.position.y)
    
        if bullet.collision(jim):
            print 'die motherfucker'
        print bullet.position.y - paul.position.y
    draw_stick_figure(screen, paul.position.x, paul.position.y)
    draw_stick_figure(screen, jim.position.x, jim.position.y)
   
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.

pygame.quit()
