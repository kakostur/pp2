import pygame
import os
import datetime

pygame.init()
done = False

window_width = 800
window_height = 800
game_display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
print(os.getcwd())

bg = pygame.image.load(os.path.normpath('mainclock.png'))
hand_second = pygame.image.load(os.path.normpath('rightarm.png'))
hand_minute = pygame.image.load(os.path.normpath('leftarm.png'))

clock_center = (window_width // 2, window_height // 2)
bg_rect = bg.get_rect(center=clock_center)
hand_second_rect = hand_second.get_rect(center=clock_center)
hand_minute_rect = hand_minute.get_rect(center=clock_center)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    time = datetime.datetime.now()

    angle_second = -(time.second * 6)
    angle_minute = -(time.minute * 6 + time.second / 10) 

    game_display.blit(bg, bg_rect)

    hand_minute_rotated = pygame.transform.rotate(hand_minute, angle_minute)
    hand_minute_rect_rotated = hand_minute_rotated.get_rect(center=clock_center)
    game_display.blit(hand_minute_rotated, hand_minute_rect_rotated.topleft)

    hand_second_rotated = pygame.transform.rotate(hand_second, angle_second)
    hand_second_rect_rotated = hand_second_rotated.get_rect(center=clock_center)
    game_display.blit(hand_second_rotated, hand_second_rect_rotated.topleft)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
