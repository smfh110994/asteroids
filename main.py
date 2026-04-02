import pygame
from constants import *
from logger import log_state, log_event
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    black = (0, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log_event("quit")
                return

        player.update(dt)
        
        screen.fill(black)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        # log state each frame (logger throttles to once per second)
        log_state()
         
if __name__ == "__main__":
    main()
