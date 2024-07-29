import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Dice Roller')

# Load dice images
dice_images = [
    pygame.image.load(f'dice{i}.png') for i in range(1, 7)
]

# Function to roll the dice
def roll_dice():
    for _ in range(10):  # Animate the roll
        number = random.randint(1, 6)
        screen.fill((255, 255, 255))  # Fill screen with white
        screen.blit(dice_images[number - 1], (150, 150))
        pygame.display.flip()
        time.sleep(0.1)
    return number

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll_dice()
    
        screen.fill((255, 255, 255))  # Fill screen with white
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
