import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    
    pygame.display.update()