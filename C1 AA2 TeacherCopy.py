import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))

paddle1 = pygame.Rect(100, 100, 50, 10)
paddle2 = pygame.Rect(300, 500, 50, 10)
ball = pygame.Rect(200, 300, 5, 5)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    pygame.draw.rect(screen, (100, 100, 100), paddle1)
    pygame.draw.rect(screen, (100, 100, 100), paddle2)
    pygame.draw.rect(screen, (0, 0, 0), ball)
    
    pygame.display.update()
