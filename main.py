import pygame
from hangman import HangMan

# Assets:
logo = pygame.image.load("Assets/logo.png")
backgroundColor = (255, 255, 102)
hangman_color = (0, 0, 0)
FPS = 60
windowSize = width, height = 600, 400
pygame.display.set_caption("HangMan")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode(windowSize)

hangMan = HangMan(6)


def draw_window():
    screen.fill(backgroundColor)
    pygame.draw.line(screen, hangman_color, (0, 0), (20, 100), 3)
    hangMan.draw_right_arm(screen)
    # We have to update the screen.
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True

    # Game loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

# this simply tells the program that game only can run from this file.
if __name__ == "__main__":
    main()

