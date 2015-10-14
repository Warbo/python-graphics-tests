#!/usr/bin/env python

import pygame
import random
import math
import sys
import time

pygame.init()
font = pygame.font.Font(None, 16)

class Toolbar:

	def __init__(self, position = (0, 550), size = (800, 50)):
		self.position = position
		self.size = size
		self.colour = (64, 64, 64)
		self.row1 = []
		self.row2 = []
		self.row1Edge = 0
		self.row2Edge = 0

	def draw(self, screen):
		pygame.draw.rect(screen, self.colour, (self.position, self.size))
		for widget in self.row1:
			widget.draw(screen)
		for widget in self.row2:
			widget.draw(screen)

	def addWidget(self, widget, row):
		if row == 1:
			widget.setPosition((self.row1Edge, self.position[1]))
			self.row1.append(widget)
			self.row1Edge += widget.size[0]
		else:
			widget.setPosition((self.row2Edge, self.position[1] + (self.size[1] / 2)))
			self.row2.append(widget)
			self.row2Edge += widget.size[0]

	def click(self, position):
		if position[1] > self.position[1] + (self.size[1] / 2):
			for widget in self.row2:
				if widget.position[0] <= position[0] and widget.position[0] + widget.size[0] > position[0]:
					widget.click()
		else:
			for widget in self.row1:
				if widget.position[0] <= position[0] and widget.position[0] + widget.size[0] > position[0]:
					widget.click()

class Widget:

	def __init__(self, size, value1, value2 = None):
		self.size = size
		self.colour = (128, 128, 128)
		self.value1 = value1
		self.value2 = value2

	def setPosition(self, position):
		self.position = position

	def click(self):
		pass

	def draw(self, screen):
		pygame.draw.rect(screen, self.colour, (self.position, self.size))

class Label(Widget):

	def draw(self, position):
		pygame.draw.rect(screen, self.colour, (self.position, self.size))
		screen.blit(font.render(self.value1, True, (255, 255, 255)), self.position)

class BrushSizeLabel(Label):

	def draw(self, position):
		global size
		pygame.draw.rect(screen, self.colour, (self.position, self.size))
		screen.blit(font.render(str(size), True, (255, 255, 255)), self.position)

class BrushButtonUp(Label):

	def click(self):
		global size
		size += 1

class BrushButtonDown(Label):

	def click(self):
		global size
		if size > 1:
			size -= 1

class RedLabel(Label):

	def draw(self, position):
		global red
		global green
		global blue
		pygame.draw.rect(screen, (red, green, blue), (self.position, self.size))
		screen.blit(font.render(str(red), True, (0, 0, 0), (255, 0, 0)), self.position)

class RedButtonUp(Label):

	def click(self):
		global red
		if red < 250:
			red += 5
		else:
			red = 255

class RedButtonDown(Label):

	def click(self):
		global red
		if red > 5:
			red -= 5
		else:
			red = 0

class GreenLabel(Label):

	def draw(self, position):
		global red
		global green
		global blue
		pygame.draw.rect(screen, (red, green, blue), (self.position, self.size))
		screen.blit(font.render(str(green), True, (0, 0, 0), (0, 255, 0)), self.position)

class GreenButtonUp(Label):

	def click(self):
		global green
		if green < 250:
			green += 5
		else:
			green = 255

class GreenButtonDown(Label):

	def click(self):
		global green
		if green > 5:
			green -= 5
		else:
			green = 0

class BlueLabel(Label):

	def draw(self, position):
		global red
		global green
		global blue
		pygame.draw.rect(screen, (red, green, blue), (self.position, self.size))
		screen.blit(font.render(str(blue), True, (0, 0, 0), (0, 0, 255)), self.position)

class BlueButtonUp(Label):

	def click(self):
		global blue
		if blue < 250:
			blue += 5
		else:
			blue = 255

class BlueButtonDown(Label):

	def click(self):
		global blue
		if blue > 5:
			blue -= 5
		else:
			blue = 0

class DottedButton(Label):

	def click(self):
		global dotted
		global smooth
		if not dotted:
			dotted = True
			smooth = False

	def draw(self, position):
		global dotted
		colour = (128, 128, 128)
		if dotted:
			colour = (64, 255, 64)
		pygame.draw.rect(screen, colour, (self.position, self.size))
		screen.blit(font.render(self.value1, True, (255, 255, 255)), self.position)

class SmoothButton(Label):

	def click(self):
		global dotted
		global smooth
		if not smooth:
			dotted = False
			smooth = True

	def draw(self, position):
		global smooth
		colour = (128, 128, 128)
		if smooth:
			colour = (64, 255, 64)
		pygame.draw.rect(screen, colour, (self.position, self.size))
		screen.blit(font.render(self.value1, True, (255, 255, 255)), self.position)

class ClearButton(Label):

	def click(self):
		self.value1 = 'Clear '

	def draw(self, screen):
		if self.value1 == 'Clear ':
			screen.fill((0, 0, 0))
			self.value1 = 'Clear'
		pygame.draw.rect(screen, self.colour, (self.position, self.size))
		screen.blit(font.render(self.value1, True, (255, 255, 255)), self.position)


if __name__ == '__main__':

	size = 1
	dotted = False
	smooth = True
	red = 255
	green = 255
	blue = 255

	screenSize = (800, 600)
	screen = pygame.display.set_mode((800, 600))
	toolbar = Toolbar()
	leftMouseHeld = False

	if True:

		toolbar.addWidget(Label((10, 25), ''), 1)

		toolbar.addWidget(Label((35, 25), 'Brush'), 1)

		toolbar.addWidget(Label((20, 25), ''), 1)

		toolbar.addWidget(Label((35, 25), 'Tools'), 1)

		toolbar.addWidget(Label((30, 25), ''), 1)

		toolbar.addWidget(Label((35, 25), 'Red'), 1)

		toolbar.addWidget(Label((11, 25), ''), 1)

		toolbar.addWidget(Label((35, 25), 'Green'), 1)

		toolbar.addWidget(Label((18, 25), ''), 1)

		toolbar.addWidget(Label((35, 25), 'Blue'), 1)

		toolbar.addWidget(Label((10, 25), ''), 2)

		toolbar.addWidget(BrushButtonDown((10, 25), '-'), 2)

		toolbar.addWidget(BrushSizeLabel((20, 25), 'X'), 2)

		toolbar.addWidget(BrushButtonUp((10, 25), '+'), 2)

		toolbar.addWidget(Label((10, 25), ''), 2)

		toolbar.addWidget(DottedButton((20, 25), '......'), 2)

		toolbar.addWidget(Label((5, 25), ''), 2)

		toolbar.addWidget(SmoothButton((20, 25), '___'), 2)

		toolbar.addWidget(Label((17, 25), ''), 2)

		toolbar.addWidget(RedButtonDown((10, 25), '-'), 2)

		toolbar.addWidget(RedLabel((20, 25), 'X'), 2)

		toolbar.addWidget(RedButtonUp((10, 25), '+'), 2)

		toolbar.addWidget(Label((10, 25), ''), 2)

		toolbar.addWidget(GreenButtonDown((10, 25), '-'), 2)

		toolbar.addWidget(GreenLabel((20, 25), 'X'), 2)

		toolbar.addWidget(GreenButtonUp((10, 25), '+'), 2)

		toolbar.addWidget(Label((10, 25), ''), 2)

		toolbar.addWidget(BlueButtonDown((10, 25), '-'), 2)

		toolbar.addWidget(BlueLabel((20, 25), 'X'), 2)

		toolbar.addWidget(BlueButtonUp((10, 25), '+'), 2)

		toolbar.addWidget(Label((10, 25), ''), 2)

		toolbar.addWidget(ClearButton((35, 25), 'Clear'), 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					sys.exit()
			elif event.type == pygame.constants.MOUSEBUTTONDOWN:
				if pygame.mouse.get_pressed()[0] == 1:
					mousePosition = pygame.mouse.get_pos()
					if mousePosition[1] < toolbar.position[1]:
						leftMouseHeld = True
						pygame.draw.line(screen, (red, green, blue), (mousePosition[0], mousePosition[1] - (size / 2)), (mousePosition[0], mousePosition[1] + (size / 2)), size)
					else:
						toolbar.click(mousePosition)
		if pygame.mouse.get_pressed()[0] == 0:
			leftMouseHeld = False
		elif pygame.mouse.get_pressed()[0] == 1:
			mousePosition = pygame.mouse.get_pos()
			leftMouseHeld = True
		if leftMouseHeld:
			relativeMovement = pygame.mouse.get_rel()
			if dotted:
				pygame.draw.line(screen, (red, green, blue), (mousePosition[0], mousePosition[1] - (size / 2)), (mousePosition[0], mousePosition[1] + (size / 2)), size)
			if smooth:
				pygame.draw.line(screen, (red, green, blue), mousePosition, (mousePosition[0] - relativeMovement[0], mousePosition[1] - relativeMovement[1]), size)
		else:
			pygame.mouse.get_rel()

		toolbar.draw(screen)
		pygame.display.update()
