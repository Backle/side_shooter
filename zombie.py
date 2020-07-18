import pygame
from pygame.sprite import Sprite
import random
from random import randint

class Zombie(Sprite):
	""" A class to represent a zombie"""

	def __init__ (self, ss_game):
		""" Initialize the zombie and set its starting position"""
		super().__init__()
		self.screen = ss_game.screen
		self.settings = ss_game.settings

		#load a random zombie image and set its rect attribute.
		image_list = ['z1.png','z2.png', 'z3.png', 'z4.png','z5.png','z6.png', 'z7.png', 'z8.png', 'z9.png']
		path = "images/zombies/"
		image = random.choice(image_list)
		image_file = f"{path}{image}"
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()

		#start each new zombie near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store the zombie's exact horizontal and vertical position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		self.zombie_speed = randint(1,5)

	def check_edge(self):
		""" Return True if zombie is at the right edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right <= screen_rect.right:
			return True

	def update(self):
		""" Move the zombie to the left """
		self.x -= self.zombie_speed
		self.rect.x = self.x