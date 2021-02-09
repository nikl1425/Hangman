import pygame


# windowSize = width, height = 600, 400

class HangMan:

    def __init__(self, lives, window, color):
        self.lives = lives
        self.window = window
        self.color = color

    def draw_man(self):
        self.draw_head()
        self.draw_Body()
        self.draw_right_arm()
        self.draw_left_leg()
        self.draw_left_arm()
        self.draw_right_leg()

    def draw_head(self):
        if self.lives <= 5:
            pygame.draw.circle(self.window, self.color, (300, 150), 10)

    def draw_Body(self):
        if self.lives <= 4:
            pygame.draw.line(self.window, self.color, (300, 160), (300, 190), 3)

    def draw_right_arm(self):
        if self.lives <= 3:
            pygame.draw.line(self.window, self.color, (300, 170), (330, 150), 3)

    def draw_left_arm(self):
        if self.lives <= 2:
            pygame.draw.line(self.window, self.color, (300, 170), (270, 150), 3)

    def draw_left_leg(self):
        if self.lives <= 1:
            pygame.draw.line(self.window, self.color, (300, 190), (270, 210), 3)

    def draw_right_leg(self):
        if self.lives <= 0:
            pygame.draw.line(self.window, self.color, (300, 190), (330, 210), 3)
