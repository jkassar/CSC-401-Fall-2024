# hw8
# Jumana Kassar
# Collaborators


# Pizza

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw8TEST.py'))

class Pizza:
    
    def __init__(self,p='M',topping=set()):
        self.size=p
        self.toppings = set(topping) if topping else set()    
    def __repr__(self):
        return f"Pizza('{self.size}',{self.toppings})"

    def getSize(self):
        return self.size

    def setSize(self, size):
        if size in ('S','M','L'):
            self.size = size

    def addTopping(self,topping):
        self.toppings.add(topping)

    def removeTopping(self,topping):
        self.toppings.discard(topping)

    def price(self):
        psize = 0
        ptop = 0
        top = self.toppings
        if self.size == 'S':
            psize += 6.25
            ptop +=.7
        elif self.size == 'L':
            psize += 12.95
            ptop += 1.85
        else:
            psize += 9.95
            ptop = 1.45
        newprice = psize + (len(top)*ptop)
        return newprice

    def __eq__(self, other):
        return self.size == other.size and self.toppings == other.toppings


def orderPizza():
    print ("Welcome to Python Pizza!")
    ans = input ("What size pizza would you like (S,M,L): ")
    pizza = Pizza(ans)
    while True:
        anstop = input('Type topping to add (or Enter to quit): ')
        if anstop == '':
            break
        else:
            pizza.addTopping(anstop)
    print("Thanks for ordering!")
    print(f"Your pizza costs ${pizza.price()}")
    return pizza



    
