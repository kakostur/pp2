import random
import pygame
import math
def main():
    screen = pygame.display.set_mode((800, 600)) 
    screen.fill((0, 0, 0)) 
    pygame.display.set_caption('Paint') 
    work_surf = pygame.Surface((800, 600)) 
    mode = 'random'
    draw_on = False
    last_pos = (0, 0) 
    color = (255, 128, 0) 
    radius = 1 
    figure = 'pen'
   
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }
    
    points = list()

    def Rect_pos(x1, y1, x2, y2):  
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) 

    def Square_pos(x1, y1, x2, y2): 
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2))

    def Equilateral_Triangle_pos(x1, y1, x2, y2): 
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x2+x2-x1, y1))
        return points

    def Right_Triangle_pos(x1, y1, x2, y2): 
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x1, y2))
        return points

    def Rhombus_pos(x1, y1, x2, y2): 
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x2-x1+x2, y1))
        points.append((x2, y1+y1-y2))
        return points

    # Игровой цикл, в котором программа продолжает цикл снова и снова, пока не произойдет событие типа QUIT
    done = False
    while not done:
        pressed = pygame.key.get_pressed()
        # alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        # ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN: 
                # if event.key == pygame.K_w and ctrl_held:
                #     pass
                # if event.key == pygame.K_F4 and alt_held:
                #     pass
                if event.key == pygame.K_1: 
                    mode = 'red'
                if event.key == pygame.K_2: 
                    mode = 'blue'
                if event.key == pygame.K_3: 
                    mode = 'green'
                if event.key == pygame.K_r:
                    figure = 'rectangle'
                if event.key == pygame.K_p: 
                    figure = 'pen'
                if event.key == pygame.K_e: 
                    figure = 'erase'
                if event.key == pygame.K_c: 
                    figure = 'circle'
                if event.key == pygame.K_s: 
                    figure = 'square'
                if event.key == pygame.K_u: 
                    figure = 'equilateral triangle'
                if event.key == pygame.K_t: 
                    figure = 'right triangle'
                if event.key == pygame.K_a: 
                    figure = 'rhombus'
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                draw_on = True # также, если зажали левую кнопку мышки, то переменная для отрисовки фигур меняет свое значение на true и переменная для определения конечных координат становится равной tuple для определения начальных координат точки
                last_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP: # если отпустили левую кнопку мыши, то переменная для отрисовки фигур снова меняет свое значение и выводим наш surface на экран
                work_surf.blit(screen, (0, 0))
                draw_on = False
            if event.type == pygame.MOUSEMOTION: # если мы двигаем мышкой, и переменная для отрисовки фигур = true, то мы проверяем, чем является фигура
                if draw_on:
                    if figure == 'pen': # если используем ручку, то рисуем линию на экране заданным цветом, от начальных координат до конечных, толщина - radius = 1
                        pygame.draw.line(screen, color, last_pos, event.pos, radius)
                        last_pos = event.pos 
                    if figure == 'erase': # если используем ластик, то рисуем черный круг на экране, центр - конечные координаты, а радиус равен 6
                        pygame.draw.circle(screen, (0, 0, 0), (event.pos[0], event.pos[1]), 6)
                    if figure == 'rectangle': # если фигура - прямоугольник, то обращаемся к функции Rect_pos, которой передаем начальные и конечные координаты, затем выводим наш surface на экран и наконец рисуем прямоугольник на экране заданным цветом согласно функции Rect_pos
                        t = Rect_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'square': # если фигура - квадрат, то обращаемся к функции Square_pos, которой передаем начальные и конечные координаты, затем выводим наш surface на экран и наконец рисуем квадрат на экране заданным цветом согласно функции Square_pos
                        t = Square_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'equilateral triangle': # если фигура - правильный треугольник, то обращаемся к функции Equilateral_Triangle_pos, которой передаем начальные и конечные координаты, затем выводим наш surface на экран и наконец рисуем правильный треугольник на экране заданным цветом согласно функции Equilateral_Triangle_pos
                        t = Equilateral_Triangle_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = [] # чистим наш лист, чтобы при следующей отрисовки он был пустым
                    if figure == 'right triangle': # если фигура - прямоугольный треугольник, то обращаемся к функции Right_Triangle_pos, которой передаем начальные и конечные координаты, затем выводим наш surface на экран и наконец рисуем прямоугольный треугольник на экране заданным цветом согласно функции Right_Triangle_pos
                        t = Right_Triangle_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = [] # чистим наш лист, чтобы при следующей отрисовки он был пустым
                    if figure == 'rhombus': # если фигура - ромб, то обращаемся к функции Rhombus_pos, которой передаем начальные и конечные координаты, затем выводим наш surface на экран и наконец рисуем ромб на экране заданным цветом согласно функции Rhombus_pos
                        t = Rhombus_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = [] # чистим наш лист, чтобы при следующей отрисовки он был пустым
                    if figure == 'circle': # если фигура - круг, то сначала выводим наш surface на экран, а затем рисуем круг на экране заданным цветом, центр - начальные координаты, радиус - расстояния между конечными и начальными координатами (формула расстояния между двумя точками)
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.circle(screen, color, (last_pos[0], last_pos[1]), int(math.sqrt((event.pos[0]-last_pos[0])**2 + (event.pos[1]-last_pos[1])**2)))

        pygame.display.flip() 
    pygame.quit() 

main() 