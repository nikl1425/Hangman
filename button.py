import pygame

# Initialize all pygame modules
pygame.init()
font = pygame.font.SysFont('Arial', 10)


def addText(window, text, posX, posY):
    window.blit(font.render(text, True, (255, 0, 0)), (posX, posY))
    pygame.display.update()


def text_onclick(text, myList):
    if pygame.mouse.get_pressed() == (1, 0, 0):
        print(text)
        return myList.append(text)


chosen_letter = []


class Button:

    def __init__(self, window, color, pressed_color, xPos, yPos, width, height, text):
        self.window = window
        self.color = color
        self.pressed_color = pressed_color
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self):
        mousePosX, mousePosY = pygame.mouse.get_pos()
        # print(mousePosX)
        pygame.draw.rect(self.window, self.color, (self.xPos, self.yPos, self.width, self.height))
        if self.xPos < mousePosX < (self.width + self.xPos) and self.yPos < mousePosY < (self.height + self.yPos):
            pygame.draw.rect(self.window, self.pressed_color, (self.xPos, self.yPos, self.width, self.height))
            text_onclick(self.text, chosen_letter)

        addText(self.window, self.text, self.xPos, self.yPos)  # Stop flickering
