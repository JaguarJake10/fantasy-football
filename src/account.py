import pygame
pygame.init()

class Account:
    def __init__(self, screen):
        self.screenNo = 0
        self.screen = screen
        self.bg = pygame.transform.scale(pygame.image.load("assets/image/football.png"), (324, 720))

    def screenNum(self):
        if self.screenNo == 0:
            self.screenNo = self.menu()
            self.screenNum()
        elif self.screenNo == 1:
            self.screenNo = self.login()
            self.screenNum()
        elif self.screenNo == 2:
            self.screenNo = self.signup()
            self.screenNum()
        else:
            pass

    