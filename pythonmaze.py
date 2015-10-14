#!/usr/bin/env python

import random
import pygame
import sys
import math
pygame.init()
try:
	import psyco
	psyco.full()
except:
	pass

screen = pygame.display.set_mode((800,600))

class VisitedException(Exception):
	pass

class OutOfBoundsException(Exception):
	pass

class Maze(object):

	def __init__(self, width, height, screen):
		"""Create a new maze with width cells across and height cells down."""
		self.width = width
		self.height = height
		self.grid = [[{'visited':False,'pending':False,'colour':0} for y in range(height)] for x in range(width)]
		self.screen = screen
		self.cell_width = 800 / self.width
		self.cell_height = 600 / self.height
		self._make_walls()
		self.topology = {}
		self.goal = None
		self._carve_cell(0,0)
		self.render()
		self._find_goal()
		self.render()

	def _make_walls(self):
		"""Used during maze creation. Creates the walls of the maze."""
		self.walls = set([])
		for x in range(self.width):
			for y in range(self.height):
				offs = [(0,0), (0,1), (1,0), (1,1)]
				for start_off in offs:
					for end_off in offs:
						print '.',
						if abs(start_off[0]-end_off[0])+abs(start_off[1]-end_off[1]) == 1:
							self.walls.add(((x+start_off[0],y+start_off[1]),(x+end_off[0],y+end_off[1])))
		new_walls = set([])
		for wall in self.walls:
			print '.',
			if (wall[1],wall[0]) in new_walls or wall in new_walls:
				continue
			new_walls.add(wall)
		self.walls = list(new_walls)
		print 'Done'

	def _get_cell(self, x, y):
		"""Used during maze creation. Returns the current state of the cell at
		coordinate (x,y)."""
		if x < 0 or y < 0 or x >= self.width or y >= self.height:
			raise OutOfBoundsException()
		return self.grid[x][y]

	def _not_visited(self, x, y):
		"""Used during maze creation. Ensures that the cell at coordinate (x, y)
		has not been visited yet."""
		self._get_cell(x, y)
		if not self.grid[x][y]['visited']:
			return
		raise VisitedException()

	def _carve_cell(self, x, y):
		"""Used during maze creation. Takes a cell coordinate and carves a path
		through it."""
		
		# We can't carve a non-existent cell. See if this cell exists
		self._get_cell(x,y)

		# We can only carve cells that haven't yet been visited
		self._not_visited(x, y)
		
		# Now that the checks are out of the way, mark ourselves as visited to
		# stop loops forming
		self.grid[x][y]['visited'] = True
		self.grid[x][y]['pending'] = True

		# Make a list of neighbour attributes (their x, their y, their position
		# relative to us and our position relative to them)
		neighbours = [{0:x,1:y-1,'us':'S','them':'N'},{0:x,1:y+1,'us':'N','them':'S'},{0:x-1,1:y,'us':'W','them':'E'},{0:x+1,1:y,'us':'E','them':'W'}]
		# To prevent bias we shuffle the neighbours
		random.shuffle(neighbours)

		# Now we loop through the neighbours to handle each one
		for index in range(4):
			# Ensure this cell exists
			try:
				self._get_cell(neighbours[index][0], neighbours[index][1])
			except OutOfBoundsException:
				continue
			# Ensure this cell hasn't been visited
			try:
				self._not_visited(neighbours[index][0], neighbours[index][1])
			except VisitedException:
				continue

			# Find the end points of this wall
			if neighbours[index]['us'] == 'S':
				corners = ((x,y),(x+1,y))
			if neighbours[index]['us'] == 'E':
				corners = ((x+1,y),(x+1,y+1))
			if neighbours[index]['us'] == 'N':
				corners = ((x,y+1),(x+1,y+1))
			if neighbours[index]['us'] == 'W':
				corners = ((x,y),(x,y+1))

			# Remove the wall from both cells
			try:
				self.walls.remove(corners)
			except ValueError:
				pass
			try:
				self.walls.remove((corners[1],corners[0]))
			except ValueError:
				pass

			# Update the view
			self._render_cell(x,y)
			self._render_walls()
			pygame.display.update()

			# Update our topology to take this path into account
			if (x,y) not in self.topology:
				self.topology[(x,y)] = set([])
			self.topology[(x,y)].add((neighbours[index][0],neighbours[index][1]))
			if (neighbours[index][0],neighbours[index][1]) not in self.topology:
				self.topology[(neighbours[index][0],neighbours[index][1])] = set([])
			self.topology[(neighbours[index][0],neighbours[index][1])].add((x,y))
			
			# Now recurse into handling this neighbour
			self._carve_cell(neighbours[index][0], neighbours[index][1])

		# Update the view
		self._render_cell(x,y)
		self._render_walls()
		pygame.display.update()
		
		# This cell is full dealt with, so it's no longer pending
		self.grid[x][y]['pending'] = False

	def render(self):
		"""Redraws this maze on the screen."""
		for x in range(self.width):
			for y in range(self.height):
				self._render_cell(x, y)
		if self.goal is not None:
			self._render_cell(self.goal[0], self.goal[1], (128,255,128))
		self._render_walls()
		pygame.display.update()

	def _render_cell(self, x, y, colour=None):
		"""Used during maze rendering. Renders a single cell of the maze."""
		# Make sure this cell exists
		self._get_cell(x,y)
		if colour is None:
			if self.grid[x][y]['visited']:
				colour = (255,255,255)
			else:
				colour = (128,128,128)
			if self.grid[x][y]['pending']:
				colour = (255,128,128)

		pygame.draw.rect(self.screen, colour, ((self.cell_width*x,self.cell_height*y),(self.cell_width,self.cell_height)), 0)

	def _render_walls(self):
		"""Used during maze rendering. Renders the walls."""
		for wall in self.walls:
			pygame.draw.line(self.screen, (0,0,0), (wall[0][0]*self.cell_width, wall[0][1]*self.cell_height), (wall[1][0]*self.cell_width, wall[1][1]*self.cell_height), 1)

	def _find_goal(self):
		"""Used during maze creation. Finds the furthest point from (0,0) and
		designates it as the goal of the maze."""
		# Start at (0,0)
		this_pass = set([(0,0)])
		# This will hold the cells we find on this pass
		next_pass = set([])
		# We start with a set of all cells and keep removing them until we have
		# 1 left
		unaccounted_for = set([])
		visited = set([])
		for x in range(self.width):
			for y in range(self.height):
				unaccounted_for.add((x,y))
		while len(unaccounted_for) > 1:
			# Visit each cell that we need to in this pass
			while len(this_pass) > 0:
				current_cell = this_pass.pop()
				# Remove it from our unvisited cell set unless it's the last one
				if len(unaccounted_for) > 1:
					unaccounted_for.discard(current_cell)
				# Add it to our visited set
				visited.add(current_cell)
				self._render_cell(current_cell[0], current_cell[1], (128,128,255))
				self._render_walls()
				pygame.display.update()
				# Mark every neighbour for traversal in the next pass, unless
				# they've already been visited
				for neighbour in self.topology[current_cell]:
					if len(unaccounted_for) > len(visited):
						if not (neighbour in visited):
							next_pass.add(neighbour)
					else:
						if neighbour in unaccounted_for:
							next_pass.add(neighbour)
			this_pass = next_pass
			next_pass = set([])
		self.goal = unaccounted_for.pop()

sys.setrecursionlimit(50*50)
maze = Maze(15,15,screen)
while True:
	maze.render()
	pygame.display.update()
