import pygame
from Circle import Circle
from Vec2 import Vec2
import math
import Contact

pygame.init() # initialized pygame

screen = pygame.display.set_mode([800,600]) # creates a window

# set up the clock
clock = pygame.time.Clock()
fps = 60
dt = 1/fps

# List of objects
objects = []

objects.append(Circle(radius=100, pos=(500,325), color=(0,0,255), vel=(0,0), mass=4))
objects.append(Circle(radius=50, pos=(200,300), color=(255,0,0), vel=(100,0), mass=1))

t = 0
running = True
while running:
    # Color the background
    screen.fill([255, 255, 255])

    for obj in objects:
        obj.clear_force()
    
    # Update velocity and position
    t += dt
    for obj in objects:
        obj.update(dt)

    # Detect contacts
    for j in range(1, len(objects)):
        for i in range(j):
            c = Contact.Bounce(objects[i], objects[j], restitution=1)
            if c:
                # The print statements demonstrate how you might do debugging
                print("before", c.a.vel, c.b.vel)
                c.resolve()
                print("after ", c.a.vel, c.b.vel)
                
    # Draw all objects
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
