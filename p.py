import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("kakos")

clock = pygame.time.Clock()
done = False 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (60, 60, 60), (60, 60, 60, 60))

    pygame.display.flip() 

    clock.tick(60)

pygame.quit()  
