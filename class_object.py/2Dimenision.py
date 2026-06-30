#Write OOP classes to handle the following scenarios:
""" A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line 
 """

class Point:

    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)

p1 = Point(0,0)
p2 = Point(1,1)

print(p1)        
print(p2)

