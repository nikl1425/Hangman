import pygame

# windowSize = width, height = 600, 400

class HangMan:
    black = (0, 0, 0)

    def __init__(self, lives):
        self.lives = lives
        self.color = HangMan.black

    def draw_head(self, window):
        pygame.draw.line(window, HangMan.black, (20, 20), (30, 30), 3)

    def draw_Body(self, window):
        pygame.draw.line(window, HangMan.black, (20, 20), (30, 30), 3)

    def draw_right_arm(self, window):
        pygame.draw.line(window, HangMan.black, (20, 20), (30, 30), 3)

    def draw_left_arm(self, window):
        pygame.draw.line(window, HangMan.black, (20, 20), (30, 30), 3)

    def draw_right_leg(self, window):
        pygame.draw.line(window, HangMan.black, (20, 20), (30, 30), 3)

    def draw_left_leg(self, window):
        pygame.draw.line(window, HangMan.black, (20, 20), (30, 30), 3)


