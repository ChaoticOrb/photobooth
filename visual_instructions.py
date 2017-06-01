#!/usr/bin/python

import pygame
from time import sleep

pygame.init()
res_w = 800 # width of camera resolution (max is 2592)
res_h = 480 # height of camera resolution (max is 1944)
img = pygame.display.set_mode((res_w,res_h), pygame.FULLSCREEN)
screen = pygame.display.get_surface()
pygame.mouse.set_visible(False)

def show_instructions():
    img = pygame.image.load('button_push.png').convert()
    screen.blit(img,(0,0))
    pygame.display.flip() # updates the whole screen
    sleep(10)

    img = pygame.image.load('countdown_explanation.png').convert()
    screen.blit(img,(0,0))
    pygame.display.flip() # updates the whole screen
    sleep(10)

    img = pygame.image.load('get_posed.png').convert()
    screen.blit(img,(0,0))
    pygame.display.flip() # updates the whole screen
    sleep(10)

    img = pygame.image.load('all_done.png').convert()
    screen.blit(img,(0,0))
    pygame.display.flip() # updates the whole screen
    sleep(10)
    pygame.quit()

print('Starting instructions')
show_instructions()
