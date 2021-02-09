import pygame
from hangman import HangMan
from button import Button
import random


# Assets:
gallow = pygame.image.load('Assets/Galge.png')
background = pygame.image.load('Assets/background.png')


# Game window config:
backgroundColor = (255, 255, 102)
FPS = 60
WIDTH = 600
HEIGHT = 400
black = (0, 0, 0)
green = (66, 245, 69)
dark_green = (43, 130, 43)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HangMan")

# Game config:
LIVES = 6

# Objects:
hangMan = HangMan(LIVES, screen, black)
easy_words = ["apple", "peach", "lemon", 'lime']
medium_words = ['pineapple', 'grapefruit', 'watermelon', 'pomegranate']
hard_words = ['blackberry', 'blood orange', 'gooseberry']
button = Button(screen, green, dark_green, 30, 30, 40, 60, 'hello')


def choose_fruit(fruitArray):
    rand_int = random.randint(0, len(fruitArray)-1)
    chosen_fruit = fruitArray[rand_int]
    # split the chosen word into letters in a list
    split_chosen_fruit = list(chosen_fruit)
    return split_chosen_fruit


print(choose_fruit(easy_words))



def draw_window():
    screen.blit(background, (0, 0))
    screen.blit(gallow, (203, 90))
    hangMan.draw_man()
    button.draw_button()
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
