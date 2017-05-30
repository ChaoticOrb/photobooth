#!/usr/bin/python

import pygame
from time import sleep

pygame.init()
res_w = 800 # width of camera resolution (max is 2592)
res_h = 480 # height of camera resolution (max is 1944)
screen = pygame.display.set_mode((res_w,res_h))
pygame.mouse.set_visible(False) #hide the mouse cursor

def show_instructions():
    surface = pygame.image.load('instructions_1.png').convert()
    pygame.display.flip() # updates the whole screen
    sleep(10)
    pygame.quit()

def clear_screen():
	screen.fill( (0,0,0) )
	pygame.display.flip()

print('Starting instructions')
show_instructions()
sleep(5)
print('Clearing screen')
clear_screen()
