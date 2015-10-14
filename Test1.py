#!/usr/bin/env python

import pygame
import os
import time
import sys
import threading
import random

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
screen = pygame.display.get_surface()
scale = 25
X = 'X'

suicide = 0

rows = {}

class Pixel:

	def __init__(self, x, y, red, green, blue):
		global scale
		self.x = x*scale
		self.y = y*scale
		self.colour = [red, green, blue]
		self.different = True
		self.clicked = False

	def draw(self, screen):
		global scale
		if self.different:
			pygame.draw.rect(screen, (self.colour[0], self.colour[1], self.colour[2]), ((self.x, self.y), (scale, scale)))
			self.different = False

	def changeColour(self, red, green, blue):
		if red == self.colour[0] and green == self.colour[1] and blue == self.colour[2]:
			pass
		else:
			self.colour = [red, green, blue]
			self.different = True

	def click(self):
		# This makes the clicked square white
		self.changeColour(255 * random.randint(0, 1), 255 * random.randint(0, 1), 255 * random.randint(0, 1))
		self.clicked = True

	#def click(self):
	#	# This is a basic action
	#	self.clicked = True

	#def click(self):
	#	# This will set the clicked pixel a 'velocity'
	#	self.velocity = [100, 500]
	#	self.clicked = True

	def cycle(self, right, topRight, top, topLeft, left, bottomLeft, bottom, bottomRight):
		# This diffuses the value of the square
		global X
		newColour = self.colour
		neighbours = [right, topRight, top, topLeft, left, bottomLeft, bottom, bottomRight]
		for neighbour in neighbours:
			for index in range(0, 3):
				if neighbour.colour[index] < self.colour[index]:
					diff = self.colour[index] - neighbour.colour[index]
					diff = diff/2
					neighbour.colour[index] += diff
					newColour[index] -= diff
		neighbour.different = True
		self.changeColour(newColour[0], newColour[1], newColour[2])

	#def cycle(self, right, topRight, top, topLeft, left, bottomLeft, bottom, bottomRight):
	#	# This forms a trail of random noise
	#	global X
	#	if self.clicked:
	#		colourChoice = random.randint(0, 2)
	#		if self.colour[colourChoice] > 190:
	#			self.colour[colourChoice] = 255
	#		else:
	#			self.colour[colourChoice] += 64
	#		self.different = True
	#		notChosen = True
	#		while notChosen:
	#			choice = random.randint(0, 3)
	#			if choice == 0:
	#				if right is X:
	#					pass
	#				else:
	#					right.click()
	#					notChosen = False
	#			if choice == 1:
	#				if top is X:
	#					pass
	#				else:
	#					top.click()
	#					notChosen = False
	#			if choice == 2:
	#				if left is X:
	#					pass
	#				else:
	#					left.click()
	#					notChosen = False
	#			if choice == 3:
	#				if bottom is X:
	#					pass
	#				else:
	#					bottom.click()
	#					notChosen = False
	#		self.clicked = False

	#def cycle(self, right, topRight, top, topLeft, left, bottomLeft, bottom, bottomRight):
	#	global X
	#	if self.clicked:
	#		self.changeColour(255, 255, 255)
	#		if self.velocity[0] > 50 and self.velocity[1] > 50:
	#			topRight.velocity = [0, 0]
	#			topRight.velocity[0] = self.velocity[0]
	#			topRight.velocity[1] = self.velocity[1] - 10
	#			topRight.clicked = True
	#		elif self.velocity[0] > 50 and self.velocity[1] < -50:
	#			bottomRight.velocity = [0, 0]
	#			bottomRight.velocity[0] = self.velocity[0]
	#			bottomRight.velocity[1] = self.velocity[1] - 10
	#			bottomRight.clicked = True
	#		elif self.velocity[0] < -50 and self.velocity[1] > 50:
	#			topLeft.velocity = [0, 0]
	#			topLeft.velocity[0] = self.velocity[0]
	#			topLeft.velocity[1] = self.velocity[1] - 10
	#			topLeft.clicked = True
	#		elif self.velocity[1] < -50 and self.velocity[1] < -50:
	#			bottomLeft.velocity = [0, 0]
	#			bottomLeft.velocity[0] = self.velocity[0]
	#			bottomLeft.velocity[1] = self.velocity[1] - 10
	#			bottomLeft.clicked = True
	#		elif self.velocity[1]**2 < self.velocity[0]**2:
	#			if self.velocity[0] < 0:
	#				left.velocity = [0, 0]
	#				left.velocity[0] = self.velocity[0]
	#				left.velocity[1] = self.velocity[1] - 10
	#				left.clicked = True
	#			elif self.velocity[0] > 0:
	#				right.velocity = [0, 0]
	#				right.velocity[0] = self.velocity[0]
	#				right.velocity[1] = self.velocity[1] - 10
	#				right.clicked = True
	#		elif self.velocity[1]**2 > self.velocity[0]**2:
	#			if self.velocity[1] > 0:
	#				top.velocity = [0, 0]
	#				top.velocity[0] = self.velocity[0]
	#				top.velocity[1] = self.velocity[1] - 10
	#				top.clicked = True
	#			elif self.velocity[1] < 0:
	#				bottom.velocity = [0, 0]
	#				bottom.velocity[0] = self.velocity[0]
	#				bottom.velocity[1] = self.velocity[1] - 10
	#				bottom.clicked = True
	#	self.clicked = False

	#def cycle(self, right, topRight, top, topLeft, left, bottomLeft, bottom, bottomRight):
	#	# This is a placeholder
	#	pass

class HandlingThread(threading.Thread):

	def run(self):
		global suicide
		global screen
		global scale
		clock = pygame.time.Clock()
		fps = 12.0
		while True:
			delta = clock.tick(fps)
			if suicide == 1:
				os.popen('kill ' + str(os.getpid()), 'r')
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					suicide = 1
					os.popen('kill ' + str(os.getpid()), 'r')
				if pygame.mouse.get_pressed()[0] == 1:
					mousePosition = pygame.mouse.get_pos()
					rows[str(mousePosition[1]/scale)][str(mousePosition[0]/scale)].click()
			pygame.display.flip()

class DrawingThread(threading.Thread):

	def run(self):
		global suicide
		global rows
		global screen
		global scale
		global width
		global height
		while True:
			for y in range((height/scale)+1):
				if suicide == 1:
					os.popen('kill ' + str(os.getpid()), 'r')
				for x in range((width/scale)+1):
					rows[str(y)][str(x)].draw(screen)
			#time.sleep(0.25)

class CyclingThread(threading.Thread):

	def run(self):
		global suicide
		global rows
		global X
		global width
		global height
		while True:
			if suicide == 1:
				os.popen('kill ' + str(os.getpid()), 'r')
			for y in range(1, (height/scale) - 2):
				for x in range(1, (width/scale) - 2):
					rows[str(y)][str(x)].cycle(rows[str(y)][str(x+1)], rows[str(y-1)][str(x+1)], rows[str(y-1)][str(x)], rows[str(y-1)][str(x-1)], rows[str(y)][str(x-1)], rows[str(y+1)][str(x-1)], rows[str(y+1)][str(x)], rows[str(y+1)][str(x+1)])
			for y in range(1, (height/scale) - 2):
				x = 0
				rows[str(y)][str(x)].cycle(rows[str(y)][str(x+1)], rows[str(y-1)][str(x+1)], rows[str(y-1)][str(x)], rows[str(y-1)][str(width/scale - 1)], rows[str(y)][str(width/scale - 1)], rows[str(y+1)][str(width/scale - 1)], rows[str(y+1)][str(x)], rows[str(y+1)][str(x+1)])
			for y in range(1, (height/scale) - 2):
				x = (width/scale)
				rows[str(y)][str(x)].cycle(rows[str(y)][str(0)], rows[str(y-1)][str(0)], rows[str(y-1)][str(x)], rows[str(y-1)][str(x-1)], rows[str(y)][str(x-1)], rows[str(y+1)][str(x-1)], rows[str(y+1)][str(x)], rows[str(y+1)][str(0)])
			y = 0
			for x in range(1, (width/scale) - 2):
				rows[str(y)][str(x)].cycle(rows[str(y)][str(x+1)], rows[str(height/scale - 1)][str(x+1)], rows[str(height/scale - 1)][str(x)], rows[str(height/scale - 1)][str(x-1)], rows[str(y)][str(x-1)], rows[str(y+1)][str(x-1)], rows[str(y+1)][str(x)], rows[str(y+1)][str(x+1)])
				pass
			y = (height/scale) - 1
			for x in range(1, (width/scale) - 2):
				rows[str(y)][str(x)].cycle(rows[str(y)][str(x+1)], rows[str(y-1)][str(x+1)], rows[str(y-1)][str(x)], rows[str(y-1)][str(x-1)], rows[str(y)][str(x-1)], rows[str(0)][str(x-1)], rows[str(0)][str(x)], rows[str(0)][str(x+1)])
				pass
			y = 0
			x = 0
			rows[str(y)][str(x)].cycle(rows[str(y)][str(x+1)], rows[str(height/scale - 1)][str(x+1)], rows[str(height/scale - 1)][str(x)], rows[str(height/scale - 1)][str(width/scale - 1)], rows[str(y)][str(width/scale - 1)], rows[str(y+1)][str(width/scale - 1)], rows[str(y+1)][str(x)], rows[str(y+1)][str(x+1)])
			y = (height/scale) - 1
			x = (width/scale) - 1
			rows[str(y)][str(x)].cycle(rows[str(y)][str(0)], rows[str(y-1)][str(0)], rows[str(y-1)][str(x)], rows[str(y-1)][str(x-1)], rows[str(y)][str(x-1)], rows[str(0)][str(x-1)], rows[str(0)][str(x)], rows[str(0)][str(0)])
			y = 0
			x = (width/scale) - 1
			rows[str(y)][str(x)].cycle(rows[str(y)][str(0)], rows[str(height/scale - 1)][str(0)], rows[str(height/scale - 1)][str(x)], rows[str(height/scale - 1)][str(x-1)], rows[str(y)][str(x-1)], rows[str(y+1)][str(x-1)], rows[str(y+1)][str(x)], rows[str(y+1)][str(0)])
			y = (height/scale) - 1
			x = 0
			rows[str(y)][str(x)].cycle(rows[str(y)][str(x+1)], rows[str(y-1)][str(x+1)], rows[str(y-1)][str(x)], rows[str(y-1)][str(width/scale - 1)], rows[str(y)][str(width/scale - 1)], rows[str(0)][str(width/scale - 1)], rows[str(0)][str(x)], rows[str(0)][str(x+1)])

if __name__ == '__main__':
	for y in range((height/scale)+1):
		rows[str(y)] = {}
		for x in range((width/scale)+1):
			rows[str(y)][str(x)] = Pixel(x, y, 0, 0, 0)
			sys.stdout.write('.')		# Give some kind of activity indicator
			sys.stdout.flush()
	colouring = DrawingThread()
	colouring.start()
	handling = HandlingThread()
	handling.start()
	cycling = CyclingThread()
	cycling.start()
	while True:
		time.sleep(1)
		if suicide == 1:
			time.sleep(1)
			sys.exit()
