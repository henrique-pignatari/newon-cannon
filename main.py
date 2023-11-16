import pygame
from bullet import Bullet
from planet import Planet
from math import atan2, sin, cos, sqrt

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
time_span = 1

middle_width = screen.get_width()/2
middle_height = screen.get_height()/2

planet_radius = 100
bullet_radius = 15

initial_force = pygame.Vector2(1.10, 0)

def calculate_gravity(bullet, planet):
  distance_vector = planet.position - bullet.position
  dx, dy = distance_vector.x, distance_vector.y
  d = sqrt(dx ** 2 + dy ** 2)
  F = bullet.mass * planet.mass / pow(d, 2)
  a = F / bullet.mass
  v = a * time_span

  theta = atan2(dy, dx)

  v_vector = pygame.Vector2(v * cos(theta), v * sin(theta))
  return v_vector

bullet = Bullet(middle_width, middle_height - planet_radius - 50, bullet_radius, initial_force)

planet = Planet(middle_width, middle_height, planet_radius)

while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    bullet.move(calculate_gravity(bullet, planet))
    screen.fill("black")
    bullet.render(screen)
    planet.render(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()