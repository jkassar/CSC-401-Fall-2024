#Week 8 Workbook



''' make this work:
p = Point() #constrSuctor
p.setx(4)
p.sety (7.1)
p.get()
p.move(1,1) #relative move modify moving it by 1,1
p.get()
'''

#v1 - all methods explicit
class Point:
    #methods are functions defined inside of a class
    #same first parameter for all methods called 'self'
    '''a Point object self has two numeric attributes
    called: self.x, self.y'''
    #if you execute p.setx(4) python wont translate it
    # p.setx(4) -> Point.setx(p, 4)
    def setx(self,xcoord):
        self.x = xcoord
        #not useless because it makes the self code know what
        #to do with the xcoord if x variable disappears
    def sety(self,ycoord):
        self.y = ycoord

    #p.get() => Point.get(p)
    def get(self):
        return (self.x, self.y)

    #p.move() -> Point.move(p,1,1)
    def move(self,deltax,deltay):
        self.x = self.x+deltax
        self.y = self.y+deltay
        ''' or you can say self.x+=deltax'''
        
    
#v2 - (gonna want this for the hw)

class Point:
    #methods are functions defined inside of a class
    #same first parameter for all methods called 'self'
    '''a Point object self has two numeric attributes
    called: self.x, self.y'''
    #this method is called the *constructor*
    # p.setx(4) -> Point.setx(p, 4)
    def __init__(self, xcoord=0,ycoord=0):
        self.x = xcoord
        self.y = ycoord

    #repr is called automatically when a string version of
    #the point self is needed
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    #good to put the repr early on in the code for debugging
    
        
    def setx(self,xcoord):
        self.x = xcoord
        #not useless because it makes the self code know what
        #to do with the xcoord if x variable disappears
    def sety(self,ycoord):
        self.y = ycoord


    #p.get() => Point.get(p)
    def get(self):
        return (self.x, self.y)


    #p1==p2 =>point.__eq__(p1,p2)
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
        #can always be rewritten
        return slef.x==other.x and self.y==other.y

    #p.move() -> Point.move(p,1,1)
    def move(self,deltax,deltay):
        self.x = self.x+deltax
        self.y = self.y+deltay
        ''' or you can say self.x+=deltax'''
        


#stand alone function
#no self arguement and not indented under tha class
def movePointAround():
    x,y = eval(input ('Enter a point: '))
    pt = Point(x,y) #  <- calls __init__
    print(pt)   # <- calls __repr__
    while True:
        ans = input('Move it how?')
        if ans == '':
            break
        else:
            dx,dy =eval(ans)
            pt.move(dx,dy)
            print(pt)   # <- calls __repr__
    return pt






    
