import pygame

FRAME_COLOR = (0, 225, 204)
SIZE_BLOCK = 20
WHITE = [255, 255, 255]
BLUE = [204, 255, 255]  # Adjusted shade of blue
size = [500, 600]
MARGIN = 1
COUNT_BLOCKS = 20

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
    screen.fill(FRAME_COLOR)

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [(MARGIN + SIZE_BLOCK) * column + MARGIN, (MARGIN + SIZE_BLOCK) * row + MARGIN, SIZE_BLOCK, SIZE_BLOCK])

    pygame.display.flip()
