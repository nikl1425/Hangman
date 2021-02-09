import pygame


def set_text(string, coordx, coordy, fontSize): #Function to set text
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)