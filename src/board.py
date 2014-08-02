import random
import pygame
from segment import Segment
from food import Food

class Board:
   def __init__(self):
      self.segments = []
      self.blockSize = 20
      self.segmentLife = 3
      self.stillPlaying = True
      self.padding = 0
      self.food = Food()
      self.score = 0

   def draw(self, screen):
      for segment in self.segments:
         segment.draw(screen)
      self.food.draw(screen)
      self.drawScore(screen) 
      
   def drawScore(self, screen):
      font = pygame.font.Font(None, 20)
      scoreText = "Score: " + str(self.score)
      text = font.render(scoreText, 1, (0, 0, 0))
      screen.blit(text, (0, 0))

   def insert(self, segment):
     self.segments.insert(0, segment)
     
   def updateSegments(self):
      survivingSegments = []
      for segment in self.segments:
         segment.update()
         if segment.life > 0:
            survivingSegments.append(segment)
      self.segments = survivingSegments

   def update(self, screen, direction='right'):
      self.updateSegments()

      if(direction == 'right'):
         self.insert(Segment(self.segments[0].x + self.blockSize+self.padding, self.segments[0].y, self.segmentLife, self.blockSize))
      elif(direction == 'left'):
         self.insert(Segment(self.segments[0].x - self.blockSize+self.padding, self.segments[0].y, self.segmentLife, self.blockSize))
      elif(direction == 'up'):
         self.insert(Segment(self.segments[0].x, self.segments[0].y - self.blockSize+self.padding, self.segmentLife, self.blockSize))
      elif(direction == 'down'):
         self.insert(Segment(self.segments[0].x, self.segments[0].y + self.blockSize+self.padding, self.segmentLife, self.blockSize))

      if (not screen.get_rect().contains(self.segments[0].getRect())) or (self.segments[0].getRect().collidelist(self.segments[1:]) != -1):
         self.stillPlaying = False

      if(self.collidingWithFood()):
         self.increaseLength(5)
         self.score += 1
         self.randomizeFood(screen)

   def collidingWithFood(self):
      return self.segments[0].getRect().colliderect(self.food.getRect())

   def increaseLength(self, length):
      self.segmentLife += length

   def randomizeFood(self, screen):
      self.food.getRect().x = random.choice(range(10, screen.get_rect().width-10))
      self.food.getRect().y = random.choice(range(10, screen.get_rect().height-10))
