import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x,self.position.y), self.radius, 2)
    
    def update(self, dt):
       self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return

        ran_ang1 = random.uniform(20,50)
        ran_ang2 = ran_ang1 * -1
        velo1 = pygame.math.Vector2.rotate(self.velocity, ran_ang1)
        velo2 = pygame.math.Vector2.rotate(self.velocity, ran_ang2)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        smal_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        smal_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        smal_ast1.velocity=velo1 * 1.2
        smal_ast2.velocity=velo2 * 1.2










