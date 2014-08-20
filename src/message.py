from textRenderer import TextRenderer

class Message:
   def __init__(self, message, x=0, y=0):
      self.x = x
      self.y = y
      self.message = message

   def draw(self, screen):
      TextRenderer.render(screen, self.message, self.x, self.y)