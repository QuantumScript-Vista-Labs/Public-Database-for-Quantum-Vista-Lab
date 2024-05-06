import tkinter as tk

def button_clicked():
    import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TERRITORY_SIZE = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Classes
class Territory:
    def __init__(self, x, y, owner=None, army=0):
        self.x = x
        self.y = y
        self.owner = owner
        self.army = army

    def draw(self, surface):
        color = WHITE
        if self.owner == "Player":
            color = GREEN
        elif self.owner == "Computer":
            color = RED
        pygame.draw.rect(surface, color, (self.x, self.y, TERRITORY_SIZE, TERRITORY_SIZE))
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.army), True, BLUE)
        surface.blit(text, (self.x + 10, self.y + 10))

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("War Game")

territories = [
    Territory(100, 100),
    Territory(300, 200),
    Territory(500, 300),
    # Add more territories as needed
]

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Drawing territories
    for territory in territories:
        territory.draw(screen)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
# Create the main UI window
root = tk.Tk()

# Create a button in the main UI
button = tk.Button(root, text="Lanch Vista Beat", command=button_clicked)
button.pack()

# Run the main event loop
root.mainloop()
