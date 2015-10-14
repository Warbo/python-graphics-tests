import pygame

class Ball:

	def __init__(self, position, size):
		self.position = position
		self.size = size

	def draw(self, screen):
		pygame.draw.rect(screen, (255, 255, 255), (self.position, (self.size, self.size)))

if __name__ == '__main__':
	pygame.init()

	screen = pygame.display.set_mode((800, 600))

	my_ball = Ball((100, 100), 50)

	my_ball.draw(screen)

	pygame.display.update()

	while True:
		pass
