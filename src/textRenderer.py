import pygame

class TextRenderer:
   @staticmethod
   def render(screen, message,x=0, y=0):
      font = pygame.font.Font(None, 20)
      text = font.render(message, 1, (0, 0, 0))
      screen.blit(text, (x, y))

   @staticmethod
   def getRenderedWidth(message):
      font = pygame.font.Font(None, 20)
      text = font.render(message, 1, (0, 0, 0))
      return font.size(message)[0]