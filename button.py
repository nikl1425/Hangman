import pygame

# Initialize all pygame modules
pygame.init()


class Button:

    def __init__(self, window, color, pressed_color, xPos, yPos, width, height):
        self.window = window
        self.color = color
        self.pressed_color = pressed_color
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height

    def draw_button(self):
        mousePosX, mousePosY = pygame.mouse.get_pos()
        print(mousePosX)
        pygame.draw.rect(self.window, self.color, (self.xPos, self.yPos, self.width, self.height))
        if self.xPos < mousePosX < (self.width + self.xPos) and self.yPos < mousePosY < (self.height + self.yPos):
            pygame.draw.rect(self.window, self.pressed_color, (self.xPos, self.yPos, self.width, self.height))

