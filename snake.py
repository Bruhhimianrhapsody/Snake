import pygame 

class Tail:

    def __init__(self, prevX, prevY):
        self.SIZE = 20 
        self.COLOR = (255, 0, 0)
        self.rect = pygame.Rect(prevX, prevY, self.SIZE, self.SIZE)

class Snake:

    def __init__(self):
        self.SIZE = 20
        self.COLOR = (255, 0, 0)
        self.head = pygame.Rect(0, 0, self.SIZE, self.SIZE)
        self.tail = [self.head]
        self.score = 0 
        self.dir = ""
        self.prevX = None
        self.prevY = None

    def draw(self, screen):
        for i in self.tail: 
            pygame.draw.rect(screen, self.COLOR, self.head)
    
    def controll(self, dir):
        if dir == "up":
            self.dir = "up"
        elif dir == "down":
            self.dir = "down"
        elif dir == "left":
            self.dir = "left"
        elif dir == "right":
            self.dir = "right"

    def move(self):
        if self.dir == "up":
            self.prevY = self.head.y
            self.head.y -= self.SIZE
        elif self.dir == "down":
            self.prevY = self.head.y
            self.head.y += self.SIZE
        elif self.dir == "left":
            self.prevX = self.head.x
            self.head.x -= self.SIZE
        elif self.dir == "right":
            self.prevX = self.head.x
            self.head.x += self.SIZE

    def check_collision(self, other):
        if self.head.x == other.rect.x and self.head.y == other.rect.y:
            other.reset()
            self.score += 1