import pygame
import random
import math
import sys
import time

pygame.init()
font = pygame.font.Font(None, 16)

step = 10

class Square:

	def __init__(self, endPosition, colour, time, size = (10, 10)):
		self.endPosition = endPosition
		self.position = [(size[0] + 2) * -1, endPosition[1]]
		self.size = size
		self.colour = colour
		self.time = time
		self.clock = 0

	def tick(self):
		self.clock += 1
		if self.clock >= self.time:
			self.trigger()

	def trigger(self):
		global step
		if self.position[0] < self.endPosition[0]:
			self.position[0] += step

	def draw(self, screen):
		pygame.draw.rect(screen, self.colour, (self.position, self.size))

if __name__ == '__main__':

	screenSize = (800, 600)
	screen = pygame.display.set_mode((800, 600))
	leftMouseHeld = False

	squares = []

	for y in range(0, 10):
		squares.append(Square((100, 50 + (10 * y)), (255, 255, 255), y * 2))

	for x in range(0, 5):
		squares.append(Square((300 + x * 10, 175), (255, 0, 0), 21 + x * 2))

	for x in range(0, 5):
		squares.append(Square((150 + x * 10, 175), (255, 0, 0), 31 + x * 2))

	for x in range(0, 9):
		squares.append(Square((130 + x * 10, 185), (255, 0, 0), 41 + x * 2))

	for x in range(0, 9):
		squares.append(Square((280 + x * 10, 185), (255, 0, 0), 60 + x * 2))

	for x in range(0, 13):
		squares.append(Square((110 + x * 10, 195), (255, 0, 0), 80 + x * 2))

	for x in range(0, 13):
		squares.append(Square((110 + x * 10, 205), (255, 0, 0), 100 + x * 2))

	for x in range(0, 13):
		squares.append(Square((260 + x * 10, 195), (255, 0, 0), 120 + x * 2))

	for x in range(0, 13):
		squares.append(Square((260 + x * 10, 205), (255, 0, 0), 140 + x * 2))

	for x in range(0, 28):
		squares.append(Square((110 + x * 10, 215), (255, 0, 0), 160 + x * 2))

	for x in range(0, 28):
		squares.append(Square((110 + x * 10, 225), (255, 0, 0), 200 + x * 2))

	for x in range(0, 28):
		squares.append(Square((110 + x * 10, 235), (255, 0, 0), 250 + x * 2))

	for x in range(0, 28):
		squares.append(Square((110 + x * 10, 245), (255, 0, 0), 300 + x * 2))

	for x in range(0, 28):
		squares.append(Square((110 + x * 10, 255), (255, 0, 0), 350 + x * 2))

	for x in range(0, 28):
		squares.append(Square((110 + x * 10, 265), (255, 0, 0), 400 + x * 2))

	for x in range(0, 28):
		squares.append(Square((110 + x * 10, 275), (255, 0, 0), 450 + x * 2))

	for x in range(0, 26):
		squares.append(Square((120 + x * 10, 285), (255, 0, 0), 500 + x * 2))

	for x in range(0, 26):
		squares.append(Square((120 + x * 10, 295), (255, 0, 0), 550 + x * 2))

	for x in range(0, 26):
		squares.append(Square((120 + x * 10, 305), (255, 0, 0), 600 + x * 2))

	for x in range(0, 24):
		squares.append(Square((130 + x * 10, 315), (255, 0, 0), 650 + x * 2))

	for x in range(0, 24):
		squares.append(Square((130 + x * 10, 325), (255, 0, 0), 700 + x * 2))

	for x in range(0, 24):
		squares.append(Square((130 + x * 10, 335), (255, 0, 0), 750 + x * 2))

	for x in range(0, 22):
		squares.append(Square((140 + x * 10, 345), (255, 0, 0), 785 + x * 2))

	for x in range(0, 20):
		squares.append(Square((150 + x * 10, 355), (255, 0, 0), 825 + x * 2))

	for x in range(0, 18):
		squares.append(Square((160 + x * 10, 365), (255, 0, 0), 860 + x * 2))

	for x in range(0, 16):
		squares.append(Square((170 + x * 10, 375), (255, 0, 0), 885 + x * 2))

	for x in range(0, 14):
		squares.append(Square((180 + x * 10, 385), (255, 0, 0), 910 + x * 2))

	for x in range(0, 12):
		squares.append(Square((190 + x * 10, 395), (255, 0, 0), 940 + x * 2))

	for x in range(0, 8):
		squares.append(Square((210 + x * 10, 405), (255, 0, 0), 960 + x * 2))

	for x in range(0, 4):
		squares.append(Square((230 + x * 10, 415), (255, 0, 0), 980 + x * 2))

	for x in range(0, 5):
		squares.append(Square((480 + x * 10, 340), (255, 255, 255), 990 + x * 2))

	for x in range(0, 4):
		squares.append(Square((560 + x * 10, 340), (255, 255, 255), 1000 + x * 2))

	for y in range(0, 10):
		squares.append(Square((500, 350 + (10 * y)), (255, 255, 255), 1010 + y * 2))

	for y in range(0, 10):
		squares.append(Square((550, 350 + (10 * y)), (255, 255, 255), 1030 + y * 2))
		squares.append(Square((600, 350 + (10 * y)), (255, 255, 255), 1030 + y * 2))

	for x in range(0, 4):
		squares.append(Square((560 + x * 10, 450), (255, 255, 255), 1050 + x * 2))

	for x in range(0, 3):
		squares.append(Square((470 + x * 10, 450), (255, 255, 255), 1060 + x * 2))

	while True:

		screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					sys.exit()
			elif event.type == pygame.constants.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0] == 1:
					mousePosition = pygame.mouse.get_pos()
					leftMouseHeld = True
		if pygame.mouse.get_pressed()[0] == 0:
			leftMouseHeld = False
		elif pygame.mouse.get_pressed()[0] == 1:
			mousePosition = pygame.mouse.get_pos()
			leftMouseHeld = True
		if leftMouseHeld:
			relativeMovement = pygame.mouse.get_rel()
		else:
			pygame.mouse.get_rel()

		for square in squares:
			square.tick()
			square.draw(screen)

		pygame.display.update()
