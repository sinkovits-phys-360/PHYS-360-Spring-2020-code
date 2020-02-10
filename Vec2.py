from math import sqrt, sin, cos
import numbers

class Vec2:
    # constructor in two different ways:
    # Vec2(list) constructs a Vec2 from a list
    # Vec2(x, y) constructs a Vec2 from x and y coordinates
    def __init__(self, x, y=None):
        if y is None:
            # hopefully x is a list of two elements
            try:
                if len(x) == 2:
                    self.x = x[0]
                    self.y = x[1]
                else:
                    raise ValueError("Incorrect single-argument instantiation for Vec2")
            except ValueError:
                raise ValueError("Incorrect single-argument instantiation for Vec2")
        else:
            self.x = x
            self.y = y
    
    # emulate a list of two elements
    # len(v) => 2
    def __len__(self):
        return 2
    # v[0] => v.x
    # v[1] => v.y
    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError("Index out of range.")

    # printed representation, returns a string
    def __repr__(self):
        return "Vec2(" + str(self.x) + ", " + str(self.y) + ")"

    # equality ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Output as a Vec2 of integers, necessary for pygame graphics
    # v.int()
    def int(self):
        return Vec2(round(self.x), round(self.y))
 
    # addition +
    def __add__(self, other):
        return Vec2(self.x + other.x,
                    self.y + other.y)
    
    # subtraction -
    def __sub__(self, other):
        return Vec2(self.x - other.x,
                    self.y - other.y)
   # negation -
    def __neg__(self):
        return Vec2(-self.x, -self.y)
    

    # scalar multiplication *
    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vec2(self.x*other,
                        self.y*other)
        else:
            raise ValueError("Can only multiply Vec2 by scalar")
    def __rmul__(self, other):
        if isinstance(other, numbers.Real):
            return Vec2(self.x*other,
                        self.y*other)
        else:
            raise ValueError("Can only multiply Vec2 by scalar")
    
    # scalar division / 
    def __truediv__(self, scalar):
        inv = 1 / scalar
        return Vec2(self.x * inv,
                    self.y * inv)

   # dot product @
    def __matmul__(self, other):
        return self.x*other.x + self.y*other.y

    # cross product %
    # returns a scalar for 2D vectors
    def __mod__(self, other):
        return ~self @ other

    # return new Vec2 rotated 90 degrees
    # v.perp()
    def perp(self):
        return Vec2(-self.y, self.x)
    # do the same but overload the ~ operator
    # ~v
    __invert__ = perp
    
    # boolean context means True for nonzero and False for zero
    def __bool__(self):
        return self.x != 0 or self.y != 0

    # magnitude squared, avoids sqrt
    def mag2(self):
        return self.x*self.x + self.y*self.y

    # magnitude
    def mag(self):
        return sqrt(self.mag2())
    # overload abs() to return magnitude
    __abs__ = mag

    # unit vector
    def hat(self):
        if self:
            return self / self.mag()
        else:
            return Vec2(0, 0)

    # return a copy
    def copy(self):
        return Vec2(self.x, self,y)

    # v.rotated(rot(radians))
    def rotated(self, rot):
        if isinstance(rot, numbers.Real):
            rot = Rotation(rot)
        return rot.transform(self)
    
# rotation class
class Rotation:
    def __init__(self, radians):
        self.sin = sin(radians)
        self.cos = cos(radians)

    def transform(self, v):
        return Vec2(v.x*self.cos - v.y*self.sin,
                    v.x*self.sin + v.y*self.cos)
