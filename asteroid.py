import pygame
from circleshape import CircleShape
from constants import SPRITE_COLOR, PLAYER_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, SPRITE_COLOR, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt