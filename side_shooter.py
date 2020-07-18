import sys
from random import randint
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from zombie import Zombie
from game_stats import GameStats
from time import sleep


class SideShooter:
	"""Overall class to manage game assets and behavior."""
	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Side Shooter")

		#create an instance to store game statistics
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.zombies = pygame.sprite.Group()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()

			if self.stats.game_active:
				self._create_hoard()
				self.ship.update()
				self._update_bullets()
				self._update_zombies()
				
			self._update_screen()
		
	def _check_events(self):
		# respond to keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses. """
		if event.key == pygame.K_UP:
			# Move the ship up.
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			# Move the ship down.
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			#Press q to quit
			sys.exit()	
		elif event.key == pygame.K_SPACE:
			#fire bullets on spacebar
			self._fire_bullet()

	def _check_keyup_events(self,event):
		""" respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		""" Create a new bullet and add it to the bullets group"""
		if len(self.bullets)< self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		""" updated bullet position and gets rid of old bullets"""
		#update bullet positons.
		self.bullets.update()
		# get rid of bullets that have dissapeared
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.settings.screen_width:
				self.bullets.remove(bullet)

	def _ship_hit(self):
		"""respond to the ship being hit by a zombie"""
		if self.stats.ships_left > 0:	
			# Decrement ships left
			self.stats.ships_left -=1

			#get rid of any remaining zombies and bullets
			self.zombies.empty()
			self.bullets.empty()

			#center the ship
			self.ship.center_ship()

			#Pause
			sleep(1.5)
		else:
			self.stats.game_active = False



	def _create_zombie(self):
		#Create a zombie and place it on the right hand side of screen
		zombie = Zombie(self)
		zombie_width, zombie_height = zombie.rect.size
		max_y = self.settings.screen_height - zombie_height
		random_entry = randint(0,max_y)
		zombie.y = random_entry
		zombie.x = (self.settings.screen_width+randint(50,200))
		zombie.rect.x = zombie.x
		zombie.rect.y = zombie.y
		self.zombies.add(zombie)

	def _create_hoard(self):
		""" Create a new bullet and add it to the bullets group"""
		if len(self.zombies)< self.settings.zombies_allowed:
			self._create_zombie()

	def _update_zombies(self):
		""" Check if a zombie is at the left edge, then update the position of all the zombies in the horde"""
		self.zombies.update()
		# get rid of zombies that have reached left edge
		for zombie in self.zombies.copy():
			if zombie.rect.right <= 0:
				self.zombies.remove(zombie)

		self._check_bullet_zombie_collision()

		#Look for zombie - ship collisions
		# Look for alien-ship collisions.
		if pygame.sprite.spritecollideany(self.ship, self.zombies):
			self._ship_hit()

		# look for zombies reaching the left edge
		self._check_zombies_left()

	def _check_bullet_zombie_collision(self):
		""" Respond to bullet zombie collisions"""
		collisions = pygame.sprite.groupcollide(self.zombies, self.bullets, True, True)
		# Check for any bullets that have hit buns.
        # If so, get rid of the bullet and the bun.

	def _check_zombies_left(self):
		"""check to see if any aliens have reached the left edge of the screen"""
		screen_rect = self.screen.get_rect()
		for zombie in self.zombies.sprites():
			if zombie.rect.left <= screen_rect.left:
				#treat this the same as if a ship got hit.
				self._ship_hit()
				break

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.zombies.draw(self.screen)
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance, and run the game.q
	ss = SideShooter()
	ss.run_game()
