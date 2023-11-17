import pygame
from math import atan2, sqrt, cos, sin

class Planet:
  def __init__(self, x, y, radius, mass, initialVelocity, color):
    self.position = pygame.Vector2(x, y)
    self.radius = radius
    self.mass = mass
    self.velocity = initialVelocity
    self.color = color

  def render(self, screen):
    self.position += self.velocity
    pygame.draw.circle(screen, self.color, self.position, self.radius)

  def calculate_gravity(self, planets):
    total_vector = pygame.Vector2(0, 0)

    for planet in planets:
      if planet == self:
        continue

      distance_vector = planet.position - self.position
      dx, dy = distance_vector.x, distance_vector.y
      d = sqrt(dx ** 2 + dy ** 2)
      F = self.mass * planet.mass / pow(d, 2)
      a = F / self.mass
      v = a

      theta = atan2(dy, dx)
      total_vector += pygame.Vector2(v * cos(theta), v * sin(theta))

    self.velocity += total_vector