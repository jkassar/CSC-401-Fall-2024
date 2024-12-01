#hw7
#Name - Jumana Kassar
#Collaborators - Shivani Chopra and Abdul Momin
#References

class Volume:

    def __init__(self,v=0):
        if v>11:
            self.v = 11
        elif v<0:
            self.v = 0
        else:
            self.v=v

    def __repr__(self):
        return f"Volume({self.v})"
    
    def set(self,v):
        if v>11:
            self.v = 11
        elif v<0:
            self.v = 0
        else:
            self.v=v

    def get(self):
        return self.v
    
    def up(self,add):
        newv = self.v + abs(add)
        if newv > 11:
            self.v = 11
        else:
            self.v = newv

    def down(self,sub):
        newv = self.v - abs(sub)
        if newv < 0:
            self.v = 0
        else:
            self.v = newv
  
    def __eq__(self,other):
        if self.v == other.v:
            return True
        else:
            return False

def partyVolume(file):
    with open(file,'r') as txtfile:
        content = txtfile.readlines()
    initial_volume = float(content[0].strip())
    newvol = Volume(initial_volume)
    for item in content[1:]:
        item = item.strip()
        if item[0]=='D':
            newvol.down(float(item[2:]))
        elif item[0]=='U':
            newvol.up(float(item[2:]))
    return newvol



if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw7TEST.py'))
