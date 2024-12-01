#queue
#FIFO data strutre


#v1 - using composition
#mantra: the list is an *attribute* of self called self.q

class Queue:
    #must write the init to create self.q
    def __init__(self,lst=[]):
        self.q =list(lst)

    def __repr__(self):
        return f'Queue({self.q})'

    
    def enqueue(self,item):
        self.q.append(item)


    #removing from the front
    def dequeue(self):
        return self.q.pop(0)
        #can have the return on a separate line as well
        


    # q[1] -> Queue.__getitem__(q, 1)
    def __getitem__(self, index):
        return self.q[index]
        #or equivalently
 #       return list.__getitem__(self.q,index)


    #we are not allowing indexed assignment
    #but if we did we would uncomment this 
    # q[1] = 'Sally' -> Queue.__setitem__(self, 1, 'Sally')
##    def __setitem__(self,index,item):
##        self.q[index] = item
##        


    #len(q) -> Queue.__len__(q)
    def __len__(self):
        return len(self.q)




    def __eq__(self,other):
        return self.q == other.q
##
##    def __add__(self, other):
##        return queue(self.q.+other.q)
##        #new list not a modifying
##        #+= is a modifyer


    #extend
    


#mantra: self IS A list instance (no self.q needed)
class MyList(list):
    '''type(self) is MyList,but self is also an instance of list class'''
    #inherit append /sort/pop/etc

    #override the repr
    def __repr__(self):
        #accumulate a string without spaces
        ans = '['
        for item in self:
            ans+= repr(item)+','
        return ans[:-1]+']'

    #using a function as an arguement
    #this is an added method, it's not in the list class
    
    def apply(self,function):
        for i in range(len(self)):
            self[i] = function (self[i])

            
