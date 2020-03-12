from Circle import Circle
from Wall import Wall


class Contact:
    def __init__(self, a, b, resolve=False, detect=None):
        # Check if detect has been specified already by user or subclass
        if detect is not None:
            self.detect = getattr(self, detect)
        else:
            # Otherwise find the correct overlap detection
            if isinstance(a, Circle) and isinstance(b, Circle):
                self.detect = self.circle_circle
            elif isinstance(a, Circle) and isinstance(b, Wall):
                self.detect = self.circle_wall
            elif isinstance(a, Wall) and isinstance(b, Circle):
                self.detect = self.circle_wall
                a, b = b, a 
            elif isinstance(a, Wall) and isinstance(b, Wall):
                self.detect = self.nothing           
            else:
                raise(ValueError, f"No overlap detection implemented between {type(a)} and {type(b)}.")
        
        # Store objects a and b
        self.a = a
        self.b = b
        
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

