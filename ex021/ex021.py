#Exercício do Ian

from playsound import playsound
playsound(r"ex021\Ela Partiu - Tim Maia.mp3")

#Exercício do Professor - Não funcionou com pygame, poré, 

import pygame
pygame.init()
pygame.mixer.music.load("ex021/Ela Partiu - Tim Maia.mp3")
pygame.event.wait()