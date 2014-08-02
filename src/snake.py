import pygame, sys
from board import Board
from segment import Segment

pygame.init()
clock = pygame.time.Clock()

screenSize = (500, 500)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('snake')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

gameBoard = Board(screen)
direction = 'right'

while True:
   screen.fill(WHITE)

   if gameBoard.stillPlaying:
      gameBoard.update(screen, direction)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
         if direction != 'left':
            direction = 'right'
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
         if direction != 'right':
            direction = 'left'
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
         if direction != 'down':
            direction = 'up'
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
         if direction != 'up':
            direction = 'down'
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
         gameBoard.increaseLength(5)

   gameBoard.draw(screen)

   pygame.display.update()
   clock.tick(10)
