class Point:
    def __init__(self, init_x, inti_y):
        self.x = init_x
        self.y = inti_y

    def __repr__(self):
        return("Point: {},{}  (x,y)".format(self.x, self.y))
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_point(self):
        return (self.x, self.y)

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distance_from_point(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2) ** 0.5

p = Point(1,1)
q = Point(5,4)
print(p.distance_from_point(q))
