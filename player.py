import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize rotation to 0 degrees
        self.rotation = 0

    def triangle(self):
        # Logic to calculate the three points of the triangle based on rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the player as a white polygon (triangle)
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)