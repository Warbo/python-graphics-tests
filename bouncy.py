#!/usr/bin/env python
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
framerate = 30
size = [10, 10]
position = [100, 50]
velocity = [500, -100]
acceleration = [0, 98]

while True:
	timeDeltaMilli = clock.tick(framerate)
	timeDelta = timeDeltaMilli / 1000.0
	if position[0] + size[0] >= 800 and velocity[0] > 0:
		velocity[0] = velocity[0] * -0.75
		velocity[1] = velocity[1] * 0.75
		position[0] = 800 - size[0]
	elif position[0] <= 0 and velocity[0] < 0:
		velocity[0] = velocity[0] * -0.75
		velocity[1] = velocity[1] * 0.75
		position[0] = 0
	if position[1] + size[1] >= 600 and velocity[1] > 0:
		velocity[0] = velocity[0] * 0.75
		velocity[1] = velocity[1] * -0.75
		position[1] = 600 - size[1]
	elif position[1] <= 0 and velocity[1] < 0:
		velocity[0] = velocity[0] * 0.75
		velocity[1] = velocity[1] * -0.75
		position[1] = 0
	velocity[0] = velocity[0] + (acceleration[0] * timeDelta)
	velocity[1] = velocity[1] + (acceleration[1] * timeDelta)
	position[0] = position[0] + (velocity[0] * timeDelta)
	position[1] = position[1] + (velocity[1] * timeDelta)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.constants.KEYDOWN:
			keyPressed = str(pygame.key.name(event.key))
			if keyPressed == 'space':
				velocity[0] += 10
				velocity[0] *= 50
				velocity[1] += 10
				velocity[1] *= 50

	pygame.draw.polygon(screen, (0, 0, 0), ((0, 0), (800, 0), (800, 600), (0, 600)), 0)
	pygame.draw.polygon(screen, (255, 255, 255), ((position[0], position[1]), (position[0] + size[0], position[1]), (position[0] + size[0], position[1] + size[1]), (position[0], position[1] + size[1])), 0)
	pygame.display.flip()
