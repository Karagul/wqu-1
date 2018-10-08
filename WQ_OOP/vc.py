'''
Created on Oct 7, 2018

@author: Charlie Victor
'''
from math import sqrt

class Point(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self, *args, **kwargs):
        return ('Point(%d, %d)' % (self.x,self.y)) 
    
    def __add__(self,other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError('Expect point to be instance of Point class. Got %s' % type(other))
        
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError('Expect point to be instance of Point class. Got %s' % type(other))
        
    def __mul__(self, a):
        if isinstance(a, (int, float)):
            return Point(self.x * a, self.y * a)
        elif isinstance(a, Point):
            return self.x * a.x + self.y * a.y
        else:
            raise TypeError('Expect point to be instance of Point class or Number class. Got %s' % type(a))
        
    def distance(self,other):
        if isinstance(other, Point):
            dx = self.x - other.x
            dy = self.y - other.y
            return sqrt(dx*dx + dy*dy) 
        else:
            raise TypeError('Expect point to be instance of Point class. Got %s' % type(other))
        
class Cluster(object):
    
    def __init__(self,x,y):
        self.center = Point(x,y)
        self.points = [self.center]
        
    def update(self):
        totalX =0
        totalY =0
        for p in self.points:
            totalX = totalX + p.x
            totalY = totalY + p.y
                    
    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
            Cluster.update(self) #update the center
        else:
            raise TypeError('Expect point to be instance of Point class. Got %s' % type(point))    
            
pointA = Point(2,3)
pointB = Point(-1,2)
print ("point A: ", pointA)
print ("point B: ", pointB)    
print ("point A + point B:", pointA + pointB)
print ("point A - point B:", pointA - pointB)
print ("point A * point B:", pointA*pointB)
print ("distance between A and B:", pointA.distance(pointB))


    
    