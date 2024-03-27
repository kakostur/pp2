import pygame
import os

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

image = pygame.image.load('mickeyclock.jpeg')
image = pygame.transform.scale(image, (400, 300))

music_directory = "/Users/karakattursynbaeva/Desktop/pp2/lab7/ex2"
os.chdir(music_directory)

music = [file for file in os.listdir() if file.endswith(".mp3")]

current_music = 0
pygame.mixer.music.load(music[current_music])
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()

    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
