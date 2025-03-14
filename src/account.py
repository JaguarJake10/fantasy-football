import pygame, sys
pygame.init()

class Account:
    def __init__(self, screen):
        self.screenNo = 0
        self.screen = screen
        self.bg = pygame.transform.scale(pygame.image.load("assets/image/football.png"), (324, 720))
        pygame.display.set_caption("Fantasy Football")

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
        elif self.screenNo == 3:
            self.screenNo == self.signupSelect()
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
        ball = pygame.transform.scale(pygame.image.load("assets/image/newball.png"), (200, 200))
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
            self.screen.blit(ball, (60, 175))
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
        user_text3 = ''
        user_text4 = ''
        text3Selected = False
        text4Selected = False
        next = pygame.font.Font("assets/font/font.ttf", 25).render("Next", True, (0, 0, 0))
        button3Hover = False
        while onSignup:
            self.screen.fill((0, 158, 5))
            pos = pygame.mouse.get_pos()
            if not (30 <= pos[0] <= 294 and 635 <= pos[1] <= 685):
                pygame.draw.rect(self.screen, (255, 255, 255), (30, 635, 264, 50), 5)
                button3Hover = False
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), (30, 635, 264, 50))
                button3Hover = True
            clock = pygame.time.Clock()
            base_font = pygame.font.Font("assets/font/font.ttf", 12)
            input_rect2 = pygame.Rect(20,200,285,42)
            input_rect3 = pygame.Rect(20,300,285,42)
            color_active = pygame.Color('black')
            color_passive = pygame.Color('black')
            colour = color_passive
            selected = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 20 <= pos[0] <= 305 and 200 <= pos[1] <= 242:
                        text3Selected = True
                        text4Selected = False
                    elif 20 <= pos[0] <= 305 and 300 <= pos[1] <= 342:
                        text3Selected = False
                        text4Selected = True
                    else:
                        text3Selected = False
                        text4Selected = False
                    print("123")
                    if button3Hover:
                        print("Yes")
                        return 3
                else:
                    selected = False
                
                if event.type == pygame.KEYDOWN:
                    if text3Selected:
                        if event.key == pygame.K_BACKSPACE:
                            user_text3 = user_text3[:-1]
                        else:
                            user_text3 += event.unicode
                    elif text4Selected:
                        if event.key == pygame.K_BACKSPACE:
                            user_text4 = user_text4[:-1]
                        else:
                            user_text4 += event.unicode
            
            if selected:
                colour = color_active
            else:
                colour = color_passive
            
            pygame.draw.rect(self.screen, colour, input_rect2)
            pygame.draw.rect(self.screen, colour, input_rect3)
            text_surface = base_font.render(user_text3, True, (255, 255, 255))
            text_surface1 = base_font.render(user_text4, True, (255, 255, 255))
            self.screen.blit(text_surface, (input_rect2.x+5, input_rect2.y+5))
            self.screen.blit(text_surface1, (input_rect3.x+5, input_rect3.y+5))
            self.screen.blit(next, (95, 650))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onSignup = False
                    return -1
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                        
            clock.tick(60)
            pygame.display.flip()



    def login(self):
        onLogin = True
        text1Selected = False
        text2Selected = False
        while onLogin:
            self.screen.fill((0, 158, 5))
            clock = pygame.time.Clock()
            base_font = pygame.font.Font("assets/font/font.ttf", 12)
            user_text1 = ''
            user_text2 = ''
            input_rect = pygame.Rect(20,200,285,42)
            input_rect1 = pygame.Rect(20,300,285,42)
            color_active = pygame.Color('black')
            color_passive = pygame.Color('black')
            colour = color_passive
            selected = False
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if 20 <= pos[0] <= 305 and 200 <= pos[1] <= 242:
                            text1Selected = True
                            text2Selected = False
                        elif 20 <= pos[0] <= 305 and 300 <= pos[1] <= 342:
                            text1Selected = False
                            text2Selected = True
                        else:
                            text1Selected = False
                            text2Selected = False
                    else:
                        selected = False
                    
                    if event.type == pygame.KEYDOWN:
                        if text1Selected:
                            if event.key == pygame.K_BACKSPACE:
                                user_text1 = user_text1[:-1]
                            else:
                                if len(user_text1) < 15:
                                    user_text1 += event.unicode
                        elif text2Selected:
                            if event.key == pygame.K_BACKSPACE:
                                user_text2 = user_text2[:-1]
                            else:
                                if len(user_text2) < 15:
                                    user_text2 += event.unicode
                
                if selected:
                    colour = color_active
                else:
                    colour = color_passive
                
                pygame.draw.rect(self.screen, colour, input_rect)
                pygame.draw.rect(self.screen, colour, input_rect1)
                text_surface = base_font.render(user_text1, True, (255, 255, 255))
                text_surface1 = base_font.render(user_text2, True, (255, 255, 255))
                self.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                self.screen.blit(text_surface1, (input_rect1.x+5, input_rect1.y+5))
                clock.tick(60)
                pygame.display.flip()

    def signupSelect(self):
        print("Gotem")
        onSelect = True
        teamSelect = pygame.font.Font("assets/font/font.ttf", 25).render("Select a team", True, (0, 0, 0))
        self.screen.blit(teamSelect, (0,0))
        while onSelect:
            self.screen.fill((0, 158, 5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onSelect = False
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()




account = Account(pygame.display.set_mode((324, 720)))
account.screenNum()
