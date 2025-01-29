import pygame
from account import *

class Graphics:
    def __init__(self):
        pygame.init()
        self.WIDTH = 324
        self.HEIGHT = 720
        self.screen=pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Fantasy Football')
        bg = pygame.transform.scale(pygame.image.load("assets/image/pitch.jpg"), (self.HEIGHT, self.WIDTH))
        self.bg = pygame.transform.rotate(bg, 90)
        self.shirt=pygame.transform.scale(pygame.image.load("assets/shirt/shirt.png"), (50, 50))
        self.shirt_locations = [(144,108), (72,180), (216,180), (144,612), (144,324), (72,360), (216,360), (36,504), (252,504), (108,540), (180,540)]
        #account = Account(self.screen)
        #account.screenNum()



    def loop(self):
        run = True
        while run == True:
            self.screen.blit(self.bg, (0, 0))
            for i in range(len(self.shirt_locations)):
                self.screen.blit(self.shirt, (self.shirt_locations[i][0] - 7, self.shirt_locations[i][1] - 7))
    
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.flip()

graphics = Graphics()
graphics.loop()