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
import numpy as np
import time
class Angle:
    def __init__(self, angle, rotation_mode):
        try:
            self.degree=float(angle)
            self.rotation_mode=int(rotation_mode)
        except ValueError:
            self.degree=90
            self.rotation_mode=0
    
    def set_rotation_mode(self, rotation_mode):
        self.rotation_mode=rotation_mode

    def set_angle(self,angle):
        angle_float=(float(angle)+179)%360-179
        self.degree=angle_float

    def get_angle(self):
        return self.degree
    
    def rotation_matrix(self):
        if self.rotation_mode==2:
            return np.array([[1,0],[0,1]])
        if self.rotation_mode==1:
            if  self.degree>0:
                return np.array([[1,0],[0,1]])
            else:
                return np.array([[-1,0],[0,1]])
        angle_rad=np.deg2rad(90-self.degree)
        return np.array([[np.cos(angle_rad),-np.sin(angle_rad)],[np.sin(angle_rad),np.cos(angle_rad)]])
    
    def turn_cw(self,angle):
        self.degree=(self.degree+angle+179)%360-179

    def turn_ccw(self,angle):
        self.degree=(self.degree-angle+179)%360-179
        
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
        '''Adds the target to the back layer'''
        self.add_target_to_front(target)
        self.start_target=target.target_id

    def add_target_to_front(self,target):
        '''
        Adds the target to the front layer
        '''
        target_at_start=self.target_dictionary[self.start_target]
        target_at_end=self.target_dictionary[target_at_start.prev_layer]
        target_at_start.prev_layer=target.target_id
        target_at_end.next_layer=target.target_id
        target.next_layer=self.start_target
        target.prev_layer=target_at_start.prev_layer
        self.target_dictionary[target.target_id]=target

    def move_target_forward_layers(self,target,n):
        pass

    def move_target_backward_layers(self,target,n):
        pass

    def set_up_iterator(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass
    
    
    
    
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
        self.graphic_effects=render_info["graphic_effects"]
        self.parent_id=parent_id
        self.is_clone=is_clone
        self.active=True
        self.game=game
        self.local_variables=local_variables
    def delete_this_clone(self):
        if self.is_clone:
            self.active=False
            self.game.targets.remove_target(self)
            self.costume_list=[None]
            self.current_costume=0
            self.local_variables=[]
            self.parent_id=None
     
    
g=Game()
g.run()
    





