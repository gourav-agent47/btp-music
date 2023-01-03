import pygame
import os

pygame.font.init()

FPS = 60

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# dimensions
HEIGHT, WIDTH = 600, 1000

#fonts
WINNER_FONT = pygame.font.SysFont('comicsans', 100)



#sprite images
image_sprite = [pygame.image.load(os.path.join('Assets','Sprite_Character','tile000.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile001.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile002.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile003.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile004.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile005.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile006.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile007.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile008.png')),
                pygame.image.load(os.path.join('Assets','Sprite_Character','tile009.png'))]

print(image_sprite)