class GameStats:
	"""Track the statistics for Side Shooter"""

	def __init__ (self, ss_game):
		""" Intitialize Statistics"""
		self.settings = ss_game.settings
		self.reset_stats()

		#start side shooter in an active state
		self.game_active = True


	def reset_stats(self):
		""" Initialize statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit