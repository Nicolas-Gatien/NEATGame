import sys
import pygame
import os

pygame.init()

# variables
CAR_SPEED = 10

W = 'w'
A = 'a'
S = 's'
D = 'd'

screen = pygame.display.set_mode((512, 512))
    # images
PLAYER_IMG = pygame.image.load('imgs/car.png').convert() 
TRACK_IMG = pygame.image.load('imgs/track.png').convert()

objects = []

screen.blit(TRACK_IMG, (0, 0))

class Car:
    def __init__(self, x, y):
        self.speed = CAR_SPEED
        self.velocity = 0
        self.rotation = 0
        self.img = PLAYER_IMG
    
    def move(self, speed, input):
        pass
        

while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
    pygame.display.update()
    pygame.time.delay(100)