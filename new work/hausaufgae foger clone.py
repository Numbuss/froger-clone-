import pygame
import os
from time import time
from typing import Any

class Settings():
    
    WINDOW = pygame.rect.Rect((0, 0), (450, 630))
    FPS = 20
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH = os.path.join(FILE_PATH, "images/")

class player (pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
      self.pos_x  = pos_x
      self.pos_y  = pos_y
      self.syse   = 90
      self.speed  = 90
      self.direktion = "top"
      super().__init__()
      self.image= pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Download_up.png")).convert()
      self.image.set_colorkey("white")
      self.image = pygame.transform.scale(self.image, (self.syse, self.syse))
      self.rect = self.image.get_rect()
      self.rect.topleft = (self.syse, self.syse)
    def update(self):
      if self.direktion   == "up":  
       self.image= pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Download_up.png")).convert()
       self.image.set_colorkey("white")
       self.image = pygame.transform.scale(self.image, (self.syse, self.syse))   
      elif self.direktion == "left":
       self.image= pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Download_left.png")).convert()
       self.image.set_colorkey("white")
       self.image = pygame.transform.scale(self.image, (self.syse, self.syse)) 
      elif self.direktion == "right":
       self.image= pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Download_right.png")).convert()
       self.image.set_colorkey("white")
       self.image = pygame.transform.scale(self.image, (self.syse, self.syse)) 
      elif self.direktion == "down":
       self.image= pygame.image.load(os.path.join(Settings.IMAGE_PATH, "Download_down.png")).convert()
       self.image.set_colorkey("white")
       self.image = pygame.transform.scale(self.image, (self.syse, self.syse)) 
      
      

class Barrier (pygame.sprite.Sprite):
       def __init__(self,pos_x,pos_y,width,movment,leftright,ship:str ):
           self.pos_x  = pos_x
           self.pos_y  = pos_y
           self.width  = width
           self.height = 90
           self.ship_image =ship
           self.movment = movment
           self.leftright = leftright

           super().__init__()
           self.image = pygame.image.load(os.path.join(Settings.IMAGE_PATH, self.ship_image)).convert()

           self.image.set_colorkey("white")
           self.image = pygame.transform.scale(self.image, (self.width, self.height))
           self.rect = self.image.get_rect()
           self.rect.topleft = (self.pos_x, self.pos_y)
       def update(self):
           if self.leftright == True:
              self.pos_x =+ self.movment
              if self.pos_x == 450:
                self.movment= self.movment * -1
                
           else:
              if self.pos_x == 450:
                 self.pos_x = 1             
        
           
           
           
           


class Game():
    def __init__(self) -> None:
               os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 50"
               pygame.init()   
               self.running = True
               self.screen = pygame.display.set_mode(Settings.WINDOW.size)
               pygame.display.set_caption("frogger clone")
               self.clock = pygame.time.Clock()
               self.all_ob = pygame.sprite.Group()
               self.ship = player(90,180)
               self.all_ships = pygame.sprite.Group()
               self.all_ships.add(self.ship)
               self.engi_ship    = Barrier(90,180,90,4,True,"Engi.png")
               self.rock_ship    = Barrier(270,90,90,2,False,"Rock.png")
               self.stealth_ship = Barrier(360,270,180,10,False,"Stealth.png")
               self.mantis_ship  = Barrier(540,75,40,3,False,"Mantis.png")
               self.mantis2_ship = Barrier(540,270,40,3,False,"Mantis.png")
               self.all_ob.add(self.engi_ship)
               self.all_ob.add(self.rock_ship)
               self.all_ob.add(self.stealth_ship)
               self.all_ob.add(self.mantis_ship)
               self.all_ob.add(self.mantis2_ship)
    def run (self):
         while self.running == True:
            self.watch_for_events()
            self.update()
            self.draw()
         

    def draw(self)-> None:
         while self.running:
            self.screen.fill("white")
            self.ship.update()
            self.all_ships.draw(self.screen)
            self.all_ob.draw(self.screen)

            pygame.display.flip()


    def watch_for_events(self)-> None:
          
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT: 
                    self.ship.direktion = "right"
                    self.ship.pos_x =+ self.ship.speed
                elif event.key == pygame.K_LEFT:
                    self.ship.direktion = "left"
                    self.ship.pos_x =- self.ship.speed
                elif event.key == pygame.K_UP:
                    self.ship.direktion = "up"
                    self.ship.pos_y =+ self.ship.speed
                elif event.key == pygame.K_DOWN:
                    self.ship.direktion = "down"
                    self.ship.pos_y =- self.ship.speed
            elif self.ship.pos_x < 0:
                 self.ship.pos_x = 0
            elif self.ship.pos_y > 630:
                 print("win")
                 self.ship.pos_x(90)
                 self.ship.pos_y(180)
            elif self.ship.pos_y > 450:
                 self.ship.pos_y = 450
            
    def update(self) -> None:
        if pygame.sprite.spritecollide(self.ship , self.all_ob):
             self.ship.direktion = "up"
             self.ship.pos_x(90)
             self.ship.pos_y(180)
    
def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
