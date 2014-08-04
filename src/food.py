import pygame
class Food:
   def __init__(self, screen, x=50, y=50, color = [0, 255, 0], blockSize=5):
      self.color = color 
      self.blockSize = blockSize
      self.rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
      self.screen = screen

   def draw(self):
      pygame.draw.rect(self.screen, self.color, self.rect)
      
   def getRect(self):
      return self.rect
