# hw2.py
# name: Jumana Kassar

def forLoops():
    for num in range (5,22,4):
        print (num)

def pay(rate,hours):
    if hours > 40:
        return (rate*40)+(rate*(hours-40)*1.5)
    else:
        return rate*hours

def abbreviation(day):
    return(day[:2])

def collision(x1,y1,r1,x2,y2,r2):
    if(r1+r2)**2 >= (x2-x1)**2 +(y1+y2)**2:
        return True
    else:
        return False

def partition(x):
    for word in x:
        if word[0] in 'ABCDEFGHIJKLM':
            print(word)
            
def lastF(first, last):
    return f"{last}, {first[0]}."



   
if __name__=='__main__':
   import doctest
   print( doctest.testfile('hw2TEST.py'))
   
