import pygame

class Display:

    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.BG_COLOR = (0,0,0)
        self.fps = 10
        self.clock = pygame.time.Clock()

    def clear(self):        
        self.screen.fill(self.BG_COLOR)
    
    def update(self):
        pygame.display.update()
        self.clock.tick(self.fps)

    def get_surface(self):
        return self.screen  