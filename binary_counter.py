import pygame
pygame.init()
import time

def iterate(screen_array, count):
	pass


screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))

screen_array = pygame.surfarray.pixels3d(screen)

count = 0
while True:
	time.sleep(0.01)
	iterate(screen_array, count)
	count += 1

#print str(2**(800*600))
