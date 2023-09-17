'''
Desafio 021 - Reproduzir Áudio MP3
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
import pygame.mixer

pygame.mixer.init()

pygame.mixer.music.load('exercicios/ex021.wav')
pygame.mixer.music.play(-1)

print('Aperte CTRL + C para interromper.')
while True:
    pass