#!/usr/bin/env python

import sys
import math
import random
import pygame
pygame.init()

class Shape(object):

	def __init__(self, sides, size):
		self.surface = pygame.Surface((size, size))
		if sides == 0:
			self.shape = pygame.draw.circle(self.surface, )
		elif sides > 2:
			self.shape = self.get_shape

def draw_lines(screen, offset):
	angle = offset
	radius = 1000
	on = True
	tick = 0
	while angle < 2*math.pi + offset:
		pygame.draw.aaline(screen, (0,0,0), (400,300), (400 + radius*math.sin(angle), 300 + radius*math.cos(angle)))
		if on:
			angle += 0.01
			tick += 0.01
		else:
			angle += 0.1
			on = True
		if tick >= 0.1:
			on = False
			tick = 0

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

offset = 0
dir = 0.01

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	draw_lines(screen, offset)
	offset = math.sin(dir)
	dir += 0.01
	if dir >= 2*math.pi:
		dir -= 2*math.pi
	elif dir <= -2*math.pi:
		dir += 2*math.pi
	pygame.display.update()
	screen.fill((255,255,255))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
