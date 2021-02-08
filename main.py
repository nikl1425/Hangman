import pygame
from hangman import HangMan
from button import Letter
import random


# Assets:
gallow = pygame.image.load('Assets/Galge.png')

# Game window config:
backgroundColor = (255, 255, 102)
FPS = 60
WIDTH = 600
HEIGHT = 400
black = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HangMan")

# Game config:
LIVES = 6

# Objects:
hangMan = HangMan(LIVES, screen, black)
easy_words = ["apple", "peach", "lemon", 'lime']
medium_words = ['pineapple', 'grapefruit', 'watermelon', 'pomegranate']
hard_words = ['blackberry', 'blood orange', 'gooseberry']



def choose_fruit(fruitArray):
    rand_int = random.randint(0, len(fruitArray))
    chosen_fruit = fruitArray[rand_int]
    return chosen_fruit

print(choose_fruit(easy_words))


def draw_window():
    screen.fill(backgroundColor)
    screen.blit(gallow, (203, 90))
    hangMan.draw_man()
    pygame.draw.rect(screen, black, (395, 0, 10, 10))


    # We have to update the screen.
    pygame.display.update()




def main():
    # Importing clock to clock
    clock = pygame.time.Clock()

    run = True

    # Game loop
    while run:
        # Setting 60 frames per second on all devices
        clock.tick(FPS)

        # Quit game proberly on completion or quiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


# this simply tells the program that game only can run from this file.
if __name__ == "__main__":
    main()
