import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    while pygame.init():
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
      screen.fill((255, 255, 255))
      pygame.display.flip()
      clock.tick(60)
      dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()

