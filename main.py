import pygame
from hangman import HangMan
from button import Button
from button import chosen_letter
from word import set_text
import random
import string

# Assets:
gallow = pygame.image.load('Assets/Galge.png')
background = pygame.image.load('Assets/background.png')
icon = pygame.image.load("Assets/logo.png")
word_font = pygame.font.SysFont('comicsans', 60)

# Game config:
backgroundColor = (255, 255, 102)
FPS = 10
WIDTH = 600
HEIGHT = 400
black = (0, 0, 0)
green = (66, 245, 69)
dark_green = (43, 130, 43)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HangMan")
pygame.display.set_icon(icon)
LIVES = 6
button_x = 30
button_y = 30

# Objects:
hangMan = HangMan(LIVES, screen, black)
easy_words = ["apple", "peach", "lemon", 'lime']
medium_words = ['pineapple', 'grapefruit', 'watermelon', 'pomegranate']
hard_words = ['blackberry', 'blood orange', 'gooseberry']
button = Button(screen, green, dark_green, 30, 30, 40, 60, 'hello')


def choose_fruit(fruitArray):
    rand_int = random.randint(0, len(fruitArray) - 1)
    chosen_fruit = fruitArray[rand_int]
    # split the chosen word into letters in a list
    #
    return chosen_fruit


def split_fruit(fruits):
    split_chosen_fruit = list(fruits)
    return split_chosen_fruit


fruit = choose_fruit(easy_words)
print(fruit)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

word = get_random_string(6)


def draw_fruit_word(actual_fruit):
    x = button_x
    for letter in (actual_fruit + word):
        b1 = Button(screen, green, dark_green, x, button_y, 40, 40, letter)
        b1.draw_button()
        x += 60
    # draw word
    display_word = ""
    for letter in fruit:
        if letter in chosen_letter:
            display_word += letter + " "
        else:
            display_word += "_ "

    text = word_font.render(display_word, 1, black)
    screen.blit(text, (200, 300))





def draw_window():
    screen.blit(background, (0, 0))
    screen.blit(gallow, (203, 90))
    hangMan.draw_man()
    draw_fruit_word(fruit)

    # We have to update the screen.


def main():
    global LIVES
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


        pygame.display.update()

    pygame.quit()


# this simply tells the program that game only can run from this file.
if __name__ == "__main__":
    main()
