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
class TargetIter:
    def __init__(self):
        self.target_dictionary={}
        self.start_target=""
    def add_initial_target(self,target):
        self.target_dictionary[target.target_id]=target
        self.start_target=target.target_id
        target.next_layer=target.target_id
        target.prev_layer=target.target_id
    def remove_target(self,target):
        if target.target_id in self.target_dictionary:
            prev_target=self.target_dictionary[target.prev_layer]
            next_target=self.target_dictionary[target.next_layer]
            prev_target.next_layer=next_target.target_id
            next_target.prev_layer=prev_target.target_id
            if self.start_target == target.target_id:
                self.start_target=next_target.target_id
            del self.target_dictionary[target.target_id]
    def add_target_to_back(self,target):
        self.add_target_to_front(target)
        self.start_target=target.target_id


    def add_target_to_front(self,target):
        target_at_start=self.target_dictionary[self.start_target]
        target_at_end=self.target_dictionary[target_at_start.prev_target]
        target_at_start.prev_layer=target.target_id
        target_at_end.next_layer=target.target_id
        target.next_target=self.start_target
        target.prev_target=target_at_start.prev_target
        self.target_dictionary[target.target_id]=target
    
    
    
class Game:
    def __init__(self):
        self.targets=[]
        self.screen=pygame.display.set_mode((480,360))
        self.running=True
        self.clock = pygame.time.Clock()

    

    def iterate_on_targets(self):
        pass

    def getuserinput(self):
        pass

    def render_targets(self):
        self.screen.fill((255,255,255))
        pygame.display.update()


    def tick(self):
        self.getuserinput()
        self.iterate_on_targets()
        self.render_targets()
    def run(self):
        while self.running:
            self.tick()
            self.clock.tick(30)
     
class Target:
    def __init__(self, render_info, parent_id, is_clone,game,local_variables,next_layer,prev_layer,target_id):
        self.x=render_info["x"]
        self.y=render_info["y"]
        self.next_layer=next_layer
        self.target_id=target_id
        self.prev_layer=prev_layer
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
    





