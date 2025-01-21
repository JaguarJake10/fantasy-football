import pygame

pygame.init()
WIDTH = 324
HEIGHT = 720
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fantasy Football')
bg = pygame.transform.scale(pygame.image.load("assets/image/pitch.jpg"), (HEIGHT, WIDTH))
bg = pygame.transform.rotate(bg, 90)
shirt=pygame.transform.scale(pygame.image.load("assets/shirt/shirt.png"), (50, 50))
shirt_locations = [(144,108), (72,180), (216,180), (144,612), (144,324), (72,360), (216,360), (36,504), (252,504), (108,540), (180,540)]

def draw_grid():
    for i in range(0, 324, 36):
        pygame.draw.line(screen, (255, 255, 255), (i, 0), (i, 720))
    for j in range(0, 720, 36):
        pygame.draw.line(screen, (255, 255, 255), (0, j), (324, j))

run = True
while run == True:
    screen.blit(bg, (0, 0))
    for i in range(len(shirt_locations)):
        screen.blit(shirt, (shirt_locations[i][0] - 7, shirt_locations[i][1] - 7))
    draw_grid()
    

    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()