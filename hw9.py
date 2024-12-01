# HW 9
#Name - Jumana Kassar


#Stack

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw9TEST.py'))

class Stack(list):
    
    def __repr__(self):
        return f"Stack({list.__repr__(self)})"
      
    def push(self,item):
        self.append(item)

    def pop(self):
        return list.pop(self,-1)

    def isEmpty(self):
        return len(self)==0

def parenthesesMatch(string):
    stack = Stack()
    pairs = {')':'(', ']':'[', '}':'{'}
    for char in string:
        if char in '[{(':
            stack.push(char)
        elif char in ']})':
            if stack.isEmpty():
                return False
            top = stack.pop()
            if top != pairs[char]:
                return False 
    return stack.isEmpty()
