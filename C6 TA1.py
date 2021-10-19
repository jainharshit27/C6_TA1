import pygame

pygame.init()

screen = pygame.display.set_mode((200, 200))

# Declare game_over and assign input() function to it with the message "Enter your name here: "
# Declare go_font and assign pygame.font.Font("freesansbold.ttf", 16)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # Declare go and assign go_font.render(game_over + ", your game is over", True, (0, 0, 0))
    # Paste the image using screen.blit(go, (100, 90))
    
    pygame.display.update()
