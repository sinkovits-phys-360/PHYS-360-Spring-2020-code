import pygame
from Circle import Circle
from Vec2 import Vec2

pygame.init() # initialized pygame

screen = pygame.display.set_mode([800,600]) # creates a window

# set up the clock
clock = pygame.time.Clock()
fps = 60
dt = 1/fps

# List of objects
objects = []

ball = Circle(radius=100, pos=Vec2(100, 300), vel=Vec2(180, 0), mass=1)
objects.append(ball)

objects.append(Circle(radius=50, pos=Vec2(400,0), vel=Vec2(0,200), mass=1))

running = True
while running:

    # Color the background
    screen.fill([255, 255, 255])

    ### Physics
    # Forces

    # Update velocity and position
    for obj in objects:
        obj.update(dt)
   
    # Draw the ball
    for obj in objects:
        obj.draw(screen)
    
    # Flip the display
    pygame.display.update()

    # limit the frame rate
    clock.tick(fps)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # clicked on close in the upper right corner
            running = False
            break

pygame.quit()  # shuts down nicely


