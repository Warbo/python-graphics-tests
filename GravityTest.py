import pygame
import os
import time
import sys
import threading
import random

class GravityWell(object):

	def __init__(self, centre, radius):
		self.centre = centre
		self.radius = radius
		self.constant = 255.0
		#self.constant = 1.0
		self.mass = 10.0

	def get_force(self, position):
		distancesquared = (position[0] - self.centre[0])**2 + (position[1] - self.centre[1])**2
		distance = distancesquared**0.5
		force = (self.constant * self.mass) / max(distance, 1e-11)
		return force

	def get_force_vector(self, position):
		distancesquared = (position[0] - self.centre[0])**2 + (position[1] - self.centre[1])**2
		distance = distancesquared**0.5
		direction = ((position[0] - self.centre[0]) / distance, (position[1] - self.centre[1]) / distance)
		force = self.constant * self.mass / max(distancesquared, 1e-11)
		#print force
		if self.centre[0] - self.radius <= position[0] <= self.centre[0] + self.radius and\
		 self.centre[1] - self.radius <= position[1] <= self.centre[1] + self.radius:
			return (0, 0)
		else:
			return (-1 * force * direction[0], -1 * force * direction[1])

class Square(object):

	def __init__(self, grid_size, size):
		square_size = (size[0] / grid_size[0], size[1] / grid_size[1])
		self.size = size
		self.wells = []
		for x in range(0, grid_size[0]):
			for y in range(0, grid_size[1]):
				self.wells.append(GravityWell(((square_size[0] / 2) + x * square_size[0], (square_size[1] / 2) + y * square_size[1]), min((self.size[0] / 2, self.size[1] / 2))))

	def get_force(self, position):
		sum = 0
		for well in self.wells:
			sum += well.get_force(position)
		return min(sum, 255)

	def get_force_vector(self, position):
		sum = [0, 0]
		for well in self.wells:
			sum[0] += well.get_force_vector(position)[0]
			sum[1] += well.get_force_vector(position)[1]
		return sum

class Mass(object):

	def __init__(self, mass, position, velocity, size):
		self.mass = mass
		self.position = position
		self.velocity = velocity
		self.size = size

	def draw(self, screen):
		pygame.draw.rect(screen, (0, 128, 255), ((self.position[0] - (self.size[0] / 2), self.position[1] - (self.size[1] / 2)), self.size))

	def apply_force(self, force):
		#f = ma
		acceleration = [0, 0]
		for dimension in range(0, 2):
			self.velocity[dimension] *= 0.5
			acceleration[dimension] = force[dimension] / self.mass
			self.velocity[dimension] += acceleration[dimension]
			self.position[dimension] += self.velocity[dimension]

if __name__ == '__main__':
	pygame.init()
	width = 800
	height = 600
	screen = pygame.display.set_mode((width, height))
	screen = pygame.display.get_surface()
	back = pygame.Surface((800, 600))
	pixel_array = pygame.surfarray.pixels3d(back)

	square = Square((3, 4), (800, 600))

	masses = []
	for x in range(10):
		masses.append(Mass((random.randint(1, 50) + 0.0) / 10.0, [random.randint(0, 800), random.randint(0, 600)], [(random.randint(-10, 10) + 0.0) / 10.0, (random.randint(-10, 10) + 0.0) / 10.0], (5, 5)))

	brightest = 0.0

	done = False
	while True:
		if not done:
			for x in range(0, width, 1):
				for y in range(0, height, 1):
					for index in range(0, 3):
						pixel_array[x][y][index] = square.get_force((x, y))
				sys.stdout.write('.')		# Give some kind of activity indicator
				sys.stdout.flush()
				#screen.blit(back, (0, 0))
				#pygame.display.update()
				#time.sleep(0.001)
			del pixel_array
			done = True
		else:
			#if mass.position[0] < 401:
			screen.blit(back, (0, 0))
			for mass in masses:
				mass.draw(screen)
				mass.apply_force(square.get_force_vector(mass.position))
			pygame.display.update()
			#print mass.velocity
			time.sleep(0.001)
			#else:
			#	print str(square.get_force_vector(mass.position))
			#time.sleep(5)
