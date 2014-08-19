import random
import pygame
from segment import Segment
from food import Food
from textRenderer import TextRenderer
from message import Message

class Board:
   def __init__(self, screen):
      self.screen = screen
      self.segments = []
      self.blockSize = 20
      self.segmentLife = 3
      self.stillPlaying = True
      self.padding = 3
      self.food = Food(self.screen)
      self.randomizeFood()
      self.score = 0
      self.insert(Segment())
      self.paused = False
      self.messages = []

   def draw(self):
      self.drawSegments()
      self.food.draw()
      self.drawScore()
      self.drawMessages()

   def drawSegments(self):
      for segment in self.segments:
         segment.draw(self.screen)

   def drawMessages(self):
      for message in self.messages:
         message.draw(self.screen)

   def drawScore(self):
      scoreText = "Score: " + str(self.score)
      TextRenderer.render(self.screen, scoreText);

   def insert(self, segment):
     self.segments.insert(0, segment)
     
   def updateSegments(self):
      survivingSegments = []
      for segment in self.segments:
         segment.update()
         if segment.life > 0:
            survivingSegments.append(segment)
      self.segments = survivingSegments

   def update(self, direction='right'):
      if self.stillPlaying and not self.paused:
         self.updateSnake(direction)
         self.draw()
      elif not self.stillPlaying:
         self.draw()
         deathMessage = "You have died. Press space to reset or q to quit."
         TextRenderer.render(self.screen, deathMessage, self.screen.get_rect().centerx - TextRenderer.getRenderedWidth(deathMessage)/2, self.screen.get_rect().centery);
      else:
         self.draw()



   def updateSnake(self, direction='right'):
      self.updateSegments()

      self.moveSnake(direction)

      if (not self.snakeIsInsideScreen(self.screen)) or (self.segments[0].getRect().collidelist(self.segments[1:]) != -1):
         self.stillPlaying = False

      if(self.collidingWithFood()):
         self.increaseLength(5)
         self.score += 1
         self.randomizeFood()

   def snakeIsInsideScreen(self, screen):
      return screen.get_rect().contains(self.segments[0].getRect())

   def moveSnake(self, direction):
      if(direction == 'right'):
         self.insert(Segment(self.segments[0].x + self.blockSize+self.padding, self.segments[0].y, self.segmentLife, self.blockSize))
      elif(direction == 'left'):
         self.insert(Segment(self.segments[0].x - self.blockSize-self.padding, self.segments[0].y, self.segmentLife, self.blockSize))
      elif(direction == 'up'):
         self.insert(Segment(self.segments[0].x, self.segments[0].y - self.blockSize-self.padding, self.segmentLife, self.blockSize))
      elif(direction == 'down'):
         self.insert(Segment(self.segments[0].x, self.segments[0].y + self.blockSize+self.padding, self.segmentLife, self.blockSize))

   def collidingWithFood(self):
      return self.segments[0].getRect().colliderect(self.food.getRect())

   def increaseLength(self, length):
      self.segmentLife += length

   def randomizeFood(self):
      self.food.getRect().x = random.choice(range(10, self.screen.get_rect().width-10))
      self.food.getRect().y = random.choice(range(10, self.screen.get_rect().height-10))
      if(self.isCollidingWithSnake(self.food)):
         self.randomizeFood()

   def isCollidingWithSnake(self, collideableObject):
      return collideableObject.getRect().collidelist(self.segments) != -1


