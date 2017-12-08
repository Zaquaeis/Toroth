import math

class Vector(object):
    def __init__(self,x,y):
        self.x = x
        self.y = x
        self.length = math.sqrt((self.x)**2 + (self.y)**2)
    
    def normalize(self):
        
        self.x = self.x/self.length
        self.y = self.y/self.length
        self.length = 1
        return 
    
    def get_normalization(self):
        x = self.x/self.length
        y = self.y/self.length
        
        return Vector(x,y)
   
    def __add__(self,vect):
        return Vector(self.x + vect.x, self.y+vect.y)
    
    def __sub__(self,vect):
        return Vector(self.x - vect.x, self.y-vect.y)
    
    
    def __eq__(self,vect):
        return self.x == vect.x and self.y==vect.y
    
    def scale(self,scalar):
        x *= scalar
        self.y *= scalar
        self.length *= scalar
    
    
    def is_near(self,vect,tolerance):
        v = self - vect
        return v.length <= tolerance
        


class Actor(object):
    def __init__(self,position,heading_vector,bounding_radius,description = None):
        self.position = Vector(position.x,position.y)
        self.heading_vector = Vector(heading_vector.x, heading_vector.y)
        self.bounding_radius = bounding_radius
        self.description = description
        
    def on_collision(self,description):
        if description == None:
            print "WEVE BEEN HIT!!!"
    def collision(self,obj):
        collision_box = min(self.bounding_radius,obj.bounding_radius)
        
        return self.position.is_near(obj.position,collision_box)
    def set_speed(self,speed):
        self.speed = speed
    
             
