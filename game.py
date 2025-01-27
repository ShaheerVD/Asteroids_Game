import pygame
from models import Spaceship
from utils import load_sprite

class SpaceRocks:
  def __init__(self):
    #initialize the game
    pygame.init()
    pygame.display.set_caption('Space Rocks')
    self.clock = pygame.time.Clock()
    
    self.screen = pygame.display.set_mode((800, 600))
    self.background = load_sprite("space", False)

    
    self.ship = Spaceship((400,300)) 

    #sprite = load_sprite("asteroid")
    #self.rock = GameObject((50,300), sprite,(0,0))

    self.collision_count = 0

  def main_loop(self):
    while True:
      self._handle_input()
      self._game_logic()
      self._draw()

  def _handle_input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()

    is_key_pressed = pygame.key.get_pressed()
    if is_key_pressed[pygame.K_ESCAPE] or is_key_pressed[pygame.K_q]:
      quit()
    elif is_key_pressed[pygame.K_RIGHT]:
      self.ship.rotate(clockwise=True)
    elif is_key_pressed[pygame.K_LEFT]:
      self.ship.rotate(clockwise=False) 
    elif is_key_pressed[pygame.K_UP]:
      self.ship.accelerate()     

  def _game_logic(self):
    self.ship.move(self.screen)
    #self.rock.move()

  def _draw(self):
    self.screen.blit(self.background, (0, 0))
    self.ship.draw(self.screen)
    #self.rock.draw(self.screen)
    pygame.display.flip()  
    self.clock.tick(30)
   ## if self.ship.collides_width(self.rock):
     ## self.collision_count += 1
      ##print(f"Collision #{self.collision_count}")
             
