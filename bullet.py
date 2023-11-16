import pygame

class Bullet:
  def __init__(self, x, y, radius, initialVelocity):
    self.position = pygame.Vector2(x, y)
    self.radius = radius
    self.mass = 1
    self.velocity = initialVelocity

  def move(self, vector): 
    self.velocity += vector

  def render(self, screen):
    self.position += self.velocity
    pygame.draw.circle(screen, "red", self.position, self.radius)