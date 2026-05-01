import pygame
from circleshape import CircleShape
from constants import *
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # 1. Always kill the current asteroid
        self.kill()

        # 2. If it's a small asteroid, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # 3. Otherwise, spawn two smaller ones
        log_event("asteroid_split")
        
        # Generate a random angle for the split
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current one
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)

        # Calculate the new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the new asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set velocities and scale them up (make them faster)
        asteroid1.velocity = new_vector_1 * 1.2
        asteroid2.velocity = new_vector_2 * 1.2