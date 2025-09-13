from screeninfo import get_monitors
import pygame
import numpy as np

# Get the primary monitor's resolution
monitor = get_monitors()[0]
monitor_width = monitor.width
monitor_height = monitor.height
total_pixels = monitor_width * monitor_height

print(f"Screen resolution: {monitor_width} x {monitor_height} pixels")
print(f"Total pixels: {total_pixels}")





n_streams = int(input("Enter the number of input variable streams\\sources: "))
dimensions = n_streams*[0]
print(dimensions)

#Set the initial location of the camera in this higher dimensional space.
cam_dim = []
def setcamloc(dimlist = dimensions):
    cam_dim = dimlist






#Area dedicated for forcing you to choose a in range screen size#
userwidth = 0
while True:  # This ensures the loop runs at least once
    userwidth = int(input("Enter the size of the screen width you want to use: ")) #Needs good break points and error catching
    if (userwidth<monitor_width) and (usewidth>2):  # The more than two is to avoid breaking
        break  # Exit the loop when the condition is met
userheight = 0
while True:  # This ensures the loop runs at least once
    userheight = int(input("Enter the the size of the screen width you want to use: ")) #Needs good break points and error catching
    if (userheight<monitor_height) and (userheight>2):  # The more than two is to avoid breaking
        break  # Exit the loop when the condition is met



screenarray = makearray(list = [userwidth,userheight])





# Initialize Pygame
pygame.init()

# Set up a 400x300 window
width, height = userwidth, userheight
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixel Manipulation with Surfarray")

# Create a surface
surface = pygame.Surface((width, height))

mymap = []

# Main loop
running = True
t = 0  # Time variable for dynamic effect
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a NumPy array for pixel manipulation
    pixels = pygame.surfarray.pixels3d(surface)
    for x in range(width):
        for y in range(height):
            pixels[x, y] =   # Dynamic gradient
    del pixels  # Unlock the surface (required for surfarray too)

    # Draw the surface to the screen
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    t += 1  # Increment time for animation

# Clean up
pygame.quit()