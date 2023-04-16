import pygame

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        #background
        self.bg = pygame.image.load('image/tietgen.png')


        # ship settings
        self.ship_limit = 0

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # alien settings
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.3

        #how quickly the aliens point increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 4.0
        self.alien_speed = 2

        #fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings for aliens and point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
