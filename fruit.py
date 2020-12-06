import pygame, random 

class Fruit():
    
    def __init__(self):
        self.SIZE = 20
        self.COLOR = (0,0,255) 
        self.x = random.randrange(0, 581, 20)
        self.y = random.randrange(0, 581, 20)
        self.rect = pygame.Rect(self.x, self.y, self.SIZE, self.SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, self.rect)
    
    def reset(self):
        self.rect.x = random.randrange(0, 581, 20)
        self.rect.y = random.randrange(0, 581, 20) 
