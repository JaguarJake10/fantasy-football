import pygame, sys
pygame.init()

class Account:
    def __init__(self, screen):
        self.screenNo = 0
        self.screen = screen
        self.bg = pygame.transform.scale(pygame.image.load("assets/image/football.png"), (324, 720))

    def screenNum(self):
        print("I am working")
        if self.screenNo == 0:
            self.screenNo = self.menu()
            self.screenNum()
        elif self.screenNo == 1:
            self.screenNo = self.login()
            self.screenNum()
        elif self.screenNo == 2:
            print("I work")
            self.screenNo = self.signup()
            self.screenNum()
        elif self.screenNo == -1:
            pygame.quit()
            sys.exit()

        else:
            pass

    def menu(self):
        onMenu = True
        button1Hover = False
        button2Hover = False
        signup = pygame.font.Font("assets/font/font.ttf", 25).render("Sign Up", True, (0, 0, 0))
        login = pygame.font.Font("assets/font/font.ttf", 25).render("Login", True, (0, 0, 0))
        titleTop = pygame.font.Font("assets/font/font.ttf", 25).render("Fantasy", True, (0, 0, 0))
        titleBottom = pygame.font.Font("assets/font/font.ttf", 25).render("Football", True, (0, 0, 0))
        ball = pygame.transform.scale(pygame.image.load("assets/image/ball.png"), (70, 70))
        while onMenu:
            self.screen.fill((0, 158, 5))
            pos = pygame.mouse.get_pos()
            if not (30 <= pos[0] <= 294 and 360 <= pos[1] <= 460):
                pygame.draw.rect(self.screen, (255, 255, 255), (30, 360, 264, 100), 5)
                button1Hover = False
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), (30, 360, 264, 100))
                button1Hover = True

            if not (30 <= pos[0] <= 294 and 490 <= pos[1] <= 590):
                pygame.draw.rect(self.screen, (255, 255, 255), (30, 490, 264, 100), 5)
                button2Hover = False
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), (30, 490, 264, 100))
                button2Hover = True
            self.screen.blit(signup, (65, 395))
            self.screen.blit(login, (90, 525))
            self.screen.blit(titleTop, (45,100))
            self.screen.blit(titleBottom, (50, 150))
            self.screen.blit(ball, (100, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onMenu = False
                    return -1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button1Hover:
                        return 2
                    elif button2Hover:
                        return 1

            pygame.display.flip()            

    def signup(self):
        onSignup = True
        while onSignup:
            self.screen.fill((0, 158, 5))
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onSignup = False
                    return -1
            pygame.display.flip()



    def login(self):
        onLogin = True
        while onLogin:
            self.screen.fill((0, 158, 5))
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onLogin = False
                    return -1
            pygame.display.flip()


account = Account(pygame.display.set_mode((324, 720)))
account.screenNum()
    