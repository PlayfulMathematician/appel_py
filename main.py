'''
Rotation Mode:
0 - All Around
1 - L/R
2 - No Rotation
'''

'''
Game Object will Render
'''
import pygame
import time

class Game:
    def __init__(self):
        self.targets=[]
        self.screen=pygame.display.set_mode((480,360))
        self.running=True
        self.clock = pygame.time.Clock()

    def reorder_targets(self):
        pass

    def iterate_on_targets(self):
        pass

    def getuserinput(self):
        pass

    def render_targets(self):
        self.screen.fill((255,255,255))
        pygame.display.update()


    def tick(self):
        self.getuserinput()
        self.reorder_targets()
        self.iterate_on_targets()
        self.reorder_targets()
        self.render_targets()
    def run(self):
        while self.running:
            self.tick()
            self.clock.tick(30)
        
class Target:
    def __init__(self, render_info, parent_id, is_clone,game,local_variables):
        self.x=render_info["x"]
        self.y=render_info["y"]
        self.costume_list=render_info["costume_list"]
        self.current_costume=render_info["current_costume"]
        self.direction=render_info["direction"]
        self.direction_style=render_info["direction_style"]
        self.visibility=render_info["visibility"]
        self.layer=render_info["layer"]
        self.graphic=render_info["graphic"]
        self.parent_id=parent_id
        self.is_clone=is_clone
        self.active=True
        self.game=game
        self.local_variables=local_variables
    def delete_this_clone(self):
        if self.is_clone:
            self.active=False
            self.costume_list=[None]
            self.current_costume=0
            self.layer=None
            self.local_variables=[]
            self.parent_id=None
     
    
g=Game()
g.run()
    





