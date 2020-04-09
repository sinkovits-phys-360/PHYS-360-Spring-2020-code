from Circle import Circle
from Wall import Wall
from Polygon import Polygon
import math
from Vec2 import Vec2

class Contact:
    def __init__(self, obj1, obj2, resolve=False, detect=None, swap=False):
        # Check if detect has been specified already by user or subclass
        if detect is not None:
            self.detect = getattr(self, detect)
        else:
            # Otherwise find the correct overlap detection
            if isinstance(obj1, Circle) and isinstance(obj2, Circle):
                self.detect = self.circle_circle
            elif isinstance(obj1, Circle) and isinstance(obj2, Wall):
                self.detect = self.circle_wall
            elif isinstance(obj1, Wall) and isinstance(obj2, Circle):
                self.detect = self.circle_wall
                swap = True
            elif isinstance(obj1, Wall) and isinstance(obj2, Wall):
                self.detect = self.nothing           
            elif isinstance(obj1, Polygon) and isinstance(obj2, Wall):
                self.detect = self.polygon_wall
            elif isinstance(obj1, Wall) and isinstance(obj2, Polygon):
                self.detect = self.polygon_wall
                swap = True
            elif isinstance(obj1, Polygon) and isinstance(obj2, Polygon):
                self.detect = self.polygon_polygon
            elif isinstance(obj1, Circle) and isinstance(obj2, Polygon):
                self.detect = self.circle_polygon
            elif isinstance(obj1, Polygon) and isinstance(obj2, Circle):
                self.detect = self.circle_polygon
                swap = True
            else:
                raise ValueError(f"No overlap detection implemented between {type(obj1)} and {type(obj2)}.")
        
        # Store objects self.obj1 and self.obj2 (first and second arguments to the overlap detection function)
        if swap:
            obj1, obj2 = obj2, obj1
        self.obj1 = obj1
        self.obj2 = obj2
        
        # Default these to self.a (meaning the penetrator) and self.b (meaning the penetrated), for times when it doesn't matter
        self.a = self.obj1
        self.b = self.obj2

        # Calculate if contact occurs
        self.detect()

        # Resolve right now, or wait till later
        if resolve:
            self.resolve(renew=False)

    def __bool__(self):
        return self.overlap > 0

    def resolve(self, renew=True):
        if renew:
            self.detect()
        return bool(self)
            
    def nothing(self):
        self.overlap = -math.inf
        self.normal = Vec2(0,0)

    def circle_circle(self):
        # Uncomment the lines below and complete them, and then remove pass
        #self.normal = 
        #self.overlap = 
        pass

    def circle_wall(self):
        # Uncomment the lines below and complete them, and then remove pass
        #self.normal = 
        #self.overlap = 
        pass

    def center_in_circle(self):
        # Uncomment the lines below and complete them, and then remove pass
        #self.normal = 
        #self.overlap = 
        pass

    def circle_in_circle(self):
        # Uncomment the lines below and complete them, and then remove pass
        #self.normal = 
        #self.overlap = 
        pass


class Push(Contact):
    def __init__(self, a, b, **kwargs):
        super().__init__(a, b, **kwargs)
    
    def resolve(self, renew=True):
        super().resolve(renew)
        return self.push()
    
    def push(self, fraction=1):
        # Complete this, then remove pass
        # Return 1 if particles get pushed apart and 0 if they don't
        pass


class Bounce(Push):
    def __init__(self, a, b, restitution=1, **kwargs):
        self.restitution = restitution
        super().__init__(a, b, **kwargs)
    
    def resolve(self, renew=True):
        super().resolve(renew)
        return self.bounce()
    
    def bounce(self):
        # Complete this, then remove pass
        # Return 1 if particles bounce and 0 if they don't
        pass

