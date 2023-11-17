import pygame
from planet import Planet

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

middle_width = screen.get_width()/2
middle_height = screen.get_height()/2

planet_radius = 80
bullet_radius = 5

bullet = Planet(middle_width, middle_height - planet_radius - 40, bullet_radius, 1, pygame.Vector2(4, 0), "blue")

planet = Planet(middle_width, middle_height, planet_radius, 1700, pygame.Vector2(0, 0), "red")

planets = [bullet, planet]

while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
       
    screen.fill("black")

    for planet in planets:
      planet.calculate_gravity(planets)
      planet.render(screen)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()