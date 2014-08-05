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

   for event in [pygame.event.poll()]:
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
         if gameBoard.stillPlaying:
            gameBoard.paused = not gameBoard.paused
         else:
            gameBoard.__init__(screen)
            direction = 'right'

   if gameBoard.stillPlaying and not gameBoard.paused:
      gameBoard.update(direction)
   elif not gameBoard.stillPlaying:
      font = pygame.font.Font(None, 20)
      deathMessage = "You have died. Press space to reset."
      text = font.render(deathMessage, 1, (0, 0, 0))
      screen.blit(text, (screen.get_rect().centerx - 125, screen.get_rect().centery))
   gameBoard.draw()

   pygame.display.update()
   clock.tick(10)
