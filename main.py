import pygame  
import sys
import display, snake, fruit 

class Run:
    
    def __init__(self):
            self.disp = display.Display()
            self.snk = snake.Snake()
            self.frt = fruit.Fruit() 
            self.run()

    def eventHandler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    self.snk.controll("up")
                if e.key == pygame.K_s:
                    self.snk.controll("down")
                if e.key == pygame.K_a:
                    self.snk.controll("left")
                if e.key == pygame.K_d:
                    self.snk.controll("right")                
                if e.key == pygame.K_x:
                    sys.exit()
                
    def run(self):
        while True: 
            self.disp.clear()

            self.eventHandler()
            
            self.snk.move()
            self.snk.draw(self.disp.get_surface())
            self.frt.draw(self.disp.get_surface())
            self.snk.check_collision(self.frt)

            print(self.frt.x)
            print(self.frt.y) 

            self.disp.update()

if __name__ == "__main__":
    Run()