import pygame
class Segment:
   def __init__(self, x=0, y=0, life=3, blockSize=5):
      self.x = x
      self.y = y
      self.blockSize = blockSize
      self.rect = pygame.Rect(self.x, self.y, self.blockSize, self.blockSize)
      self.life = life

   def __str__(self):
      return "x: "+str(self.x)+", y: "+str(self.y)

   def draw(self, screen):
      pygame.draw.rect(screen, (255, 0, 0), self.rect)

   def update(self):
      self.life -= 1

   def getRect(self):
      return self.rect
