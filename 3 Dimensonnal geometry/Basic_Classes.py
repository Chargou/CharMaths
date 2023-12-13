class Point():
    """Point in a 3D space"""
    def __init__(x=0, y=0, z=0):
        assert sametype(x, y, z) and (type(x)==int or type(x)==float), "Please provide real numbers"
        self.x = x
        self.y = y
        self.z = z
    
    def __eg__(self, other):
        assert type(other)
        return self.x==other.x and self.y==other.y and self.z==other.z
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)

    def is_aligned_with(self, other, other2):
        """Returns True if self, other, and other2 are aligned
        the three must be Points"""
        assert sametype(self, other, other2) and type(self) == "Point", "please provide Points"
        return Vector(self, other).is_colinear_with(Vector(self, other2)
    

class Vecteur():
    def __init__(x=0, y=0, z=0):
        """May be created using 3 reals or 2 points"""
        if sametype(x, y, z) and (type(x)==int or type(x)==float):
            self.x = x
            self.y = y
            self.z = z
        elif type(x) == type(y) and type(x) == 'Point' and z==0:
            a = y-x
            self.x = a.x
            self.y = a.y
            self.z = a.z
        else:
            assert False, "error with your arguments"
    
    def normalise(self):
        pass

    def is_colinear_with(self, other):
        """returns True if self and other are colinear
        self and other must be Vectors""" 
        assert type(self) == "Vector" and type(other) == "Vector", "please provide vectors"
        return self.x*other.y == self.y*other.x and self.z*other.y == self.y*other.z and self.x*other.z == self.z*other.x
    

class Line():
    pass

class Plane():
    pass

def sametype(a, b, c):
    return type(a) == type(b) and type(a) == type(c)
