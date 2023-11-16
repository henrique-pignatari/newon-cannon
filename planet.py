import pygame

class Planet:
  def __init__(self, x, y, radius):
    self.position = pygame.Vector2(x, y)
    self.radius = radius
    self.mass = 200

  def render(self, screen):
    pygame.draw.circle(screen, "blue", self.position, self.radius)