import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	""" A class to manage bullets fired from the ship"""
	def __init__(self, ss_game):
		"""create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.color = self.settings.bullet_color

		# create a bullet at rect (0,0) and then set the correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		#gun_aduster = int(ss_game.ship.rect.y) + 0
		gun_aduster = int(ss_game.ship.rect.y) + 54
		self.rect.midright = (ss_game.ship.rect.right, gun_aduster)

		#store the bullet's position as a decimal value
		self.x = float(self.rect.x)

	def update(self):
		"""Move the bullet up the screen"""
		#update the decimal position of the bullet.
		self.x +=self.settings.bullet_speed
		#update the rect positon.
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
