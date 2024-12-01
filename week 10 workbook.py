#Week 10

#inheritance - not covered on the final
#but will be used for hw9

#can use inheritance to define a custom exception class
class CuttingError(Exception):
    pass

#v2 of queue class with Inheritance

#MyList inherits from list type(self) is Queue but
#self is also a list instance

#mantra: Self IS a list instance
class Queue(list):
    #inherits __init__, often this works
    #inherits __getitem__, __len__, __eq__

    #extend repr
    def __repr__(self):
        #list class repr
        return f"Queue ({list.__repr__(self)})"
        #return f'Queue({self})' = causes infinite recursion error
    
    #added methods
    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    # inherits __getitem__

    def __setitem__(self, index, item):
        #want this to cause an error
        raise TypeError('Queue does not support indexed assignment')
        #raise CuttingError('Queue does not support indexed assignment')
            #CuttingError is renamed from the class Cutting error above

    def __add__(self,other):
        return Queue(list.__add__(self,other))
    
    
