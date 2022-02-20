from operator import truediv
import pygame
import math

pygame.init()

FRAMES_PER_TICK = 60
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Orbit Sim")

WHITE = (255,255,255)
YELLOW = (255, 255, 0)

class Planet:
    
    AU = 149.6e6 * 1000     # astronomical unit, the approximate distance from the earth to the sun
    G = 6.67428e-11         # gravitational constant
    SCALE = 250 / AU        # 1 AU = 100 pixels
    TIMESTEP = 3600 * 24    # seconds in an hour * hours in a day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        pygame.draw.circle(win, self.color, (x,y), self.radius)



def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    planets = [sun]

    while run:
        # setting clock speed
        clock.tick(FRAMES_PER_TICK)
        # WIN.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.draw(WIN)
        
        pygame.display.update()
    
    pygame.quit()

main()
