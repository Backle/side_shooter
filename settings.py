

class Settings:
	"""A class to store all settings for Side Shooter."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (3, 41, 120)

		#Ship Settings
		self.ship_speed = 10
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 10.0
		self.bullet_width = 15
		self.bullet_height = 5
		self.bullet_color = (191, 122, 70)
		self.bullets_allowed = 3
		self.zombies_allowed = 10

