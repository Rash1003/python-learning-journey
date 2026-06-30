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

    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))


class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.A,self.B,self.C)


""" p1 = Point(3,6)
p2 = Point(8,-5)
 """
l1 = Line(1,2,1)
print(l1)


""" print(p1)        
print(p2)
dist = p1.euclidean_distance(p2)
print(dist)

origin = p2.distance_from_origin()
print(origin) """