import pygame
import sys
import random
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()

SW, SH = 550, 550

BLOCK_SIZE = 30
BLOCK = 75
font = pygame.font.SysFont("Verdana", 20)
FONT = pygame.font.SysFont("Verdana", 20)

lev = 1
scr = 0

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()
fps = 5

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        global apple
        global lev
        global scr

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH + 50):
                self.dead = True

        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            lev = 1
            scr = 0
            apple = Apple()

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):#updating rectangle's place
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
class big_apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK, BLOCK)

    def update(self): #updating rectangle's place
        self.x = int(random.randint(0, SW) / BLOCK) * BLOCK
        self.y = int(random.randint(0, SH) / BLOCK) * BLOCK
        self.rect = pygame.Rect(self.x, self.y, BLOCK, BLOCK)

    def blink(self):# making rectange blink
        a = random.choice([-5,+5])
        self.rect = pygame.Rect(self.x - a/2, self.y - a/2, BLOCK + a, BLOCK + a)
    def end(self): # moving big apple to place where it cannot be seen
        self.x = -2000
        self.y = -2000
        self.rect = pygame.Rect(self.x, self.y, BLOCK, BLOCK)
# Setting up Sprites
snake = Snake()
apple = Apple()
bigapple = big_apple()





# шкала левала и score
score = FONT.render("1", True, "white")
level = font.render("level: " + str(lev), True, (255,255,255))
score_rect = score.get_rect(center=(SW / 2, SH / 20))
screen.blit(level, (150, 10))
timer = 0

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 3000)

while True:
    timer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
    snake.update()

    screen.fill('black')

    pygame.draw.rect(screen, "green", snake.head)
    temp = 0
    for square in snake.body:
        pygame.draw.rect(screen, (0,255,temp), square)
        if temp+5 >= 255:
            temp = temp
        else:
            temp += 5
    pygame.draw.rect(screen, "orange", apple.rect)
    pygame.draw.rect(screen, RED, bigapple.rect)
    score = FONT.render("score: "+ str(scr), True, "white")
    level = font.render("level: " + str(lev), True, (255, 255, 255))
    screen.blit(score, (150, 10))
    screen.blit(level, (300, 10))
    bigapple.blink()
    if timer%30 == 0:
        bigapple.end()
    if snake.head.colliderect(apple.rect):
        scr += 1
        apple.update()
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))

        if scr % 10 == 0 and scr != 0:
            timer = 1
            bigapple.update()

    for rect in snake.body:
        if rect.colliderect(apple.rect):
            scr +=1
            apple.update()
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            if scr % 10 == 0 and scr!=0:
                bigapple.update()
                timer = 1
        if rect.colliderect(bigapple.rect):
            bigapple.end()
            scr += 3
            fps += 1
            for i in range(3):
                snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
            lev += 1
    if snake.head.colliderect(bigapple.rect):
        bigapple.end()
        scr += 3
        fps += 1
        for i in range(3):
            snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        lev +=1
    pygame.display.update()
    clock.tick(fps)