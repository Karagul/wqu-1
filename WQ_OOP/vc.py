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
    
    center = Point(0,0)
    points = []
    
    def __init__(self,x,y):
        self.center = Point(x,y)
        self.points.append(self.center)
        
    def update(self):
        totalX =0
        totalY =0
        numPoints = len(self.points)
        for p in self.points:
            totalX = totalX + p.x
            totalY = totalY + p.y
        
        self.center = Point(totalX / numPoints, totalY/ numPoints) #this is the new center    
                    
    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
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


points = [(1,2), (-2,3), (-5,7), (3,4), (-7,-1), (-10,5), (0,0)]

def compute_result(points):
    points = [Point(*point) for point in points]
    a = Cluster(1,0)
    b = Cluster(-1,0)
    a_old = []
    for _ in range(10000): # max iterations
        
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                # add the right point
                    a.add_point(point)
            else:
                # add the right point
                    b.add_point(point)
                    
        if a_old == a.points:
            break
        else:
            a_old = a.points
        
        a.update()
        b.update()
    
    # For testing purpose
    print ("Cluster a:", a.points)
    print ("Cluster b:", b.points)
    print ("New centroids: ", [(a.center.x,a.center.y),(b.center.x,b.center.y)])
    
    # Return the result (sorted) to the grader
    if (a.center.x > b.center.x):
        return [(a.center.x,a.center.y),(b.center.x,b.center.y)]
    else:
        return [(b.center.x,b.center.y),(a.center.x,a.center.y)]   
    
compute_result(points)    
    