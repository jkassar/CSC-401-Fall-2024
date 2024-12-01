# week4.py

'''
make this work:

>>> oddEven( [22,33,44] )
even
odd
even
'''

# print version
def oddEven( numlst ):
    for num in numlst:
        if num%2==0: # even
            print('even')
        else:
            print('odd')

# return version
def oddEven( numlst ):
    for num in numlst:
        if num%2==0: # even
            return 'even'
        else:
            return 'odd'


'''
>>> total( [3,12,6,22] )
43
'''

# accumulation
def total( numlst ):
    # 1 - initialize before the loop
    runningTotal = 0
    # 0 - print version
    # iterate through the numbers
    for num in numlst:
        # print( num )
        # 2 - accumulate in the loop
        # runningTotal = runningTotal + num
        runningTotal += num
        # print( vars() )
    # 3 - return after the loop
    return runningTotal
        
'''
>>> countNegs( [2,-5,-23,44,2] )
2
'''

def countNegs( numlst ):
    # 1
    count = 0 # count of negative numbers

    # 0 
    for num in numlst:
        if num<0:
            # print( num )
            # 2
            count += 1
    # 3
    return count
            


'''
>>> negatives( [2,-5,-23,44,2] )
[-5, -23]
'''

def negatives(numlst):
    # 1
    ans = []
    #0
    for num in numlst:
        if num<0:
            # print( num )
            # 2
            ans.append( num )
    # 3
    return ans

'''
make this work:

>>> stripPunct("How, are you?!")
'How are you'
'''

def stripPunct( phrase ):
    ans = ''
    for char in phrase:
        if char not in '.,;?!:':
            #print( char )
            ans += char
            print( ans )
    return ans

def stripPunct( phrase ):

    for punct in '.,;?!:':
        phrase = phrase.replace(punct,'')
        print( phrase )
    return phrase

'''
want this to work:

>>> hasVowel("hello how are you?")
True
>>> hasVowel("lfkjsdjfldjsf")
False
'''

# search
def hasVowel( string ):

    for char in string:
        if char in 'aeiou':
            return True
       
    return False

'''
>>> vowelIndices( 'hello, you are you?')
[1,4,...]
'''

# indexed accumulator
def vowelIndices( phrase ):
    indices = []
    for i in range(len(phrase)):
        # if vowel
        if phrase[i] in 'aeiou':
            # print( i, phrase[i] )
            indices.append(i)
    return indices

'''
make this work:

>>> firstVowel('hello, how are you?')
1 # index of "e" first vowel
>>> firstVowel('jdjsdjfj')
-1 # no vowel found
'''

# indexed search
def firstVowel( phrase ):

    for i in range(len(phrase)):
        if phrase[i] in 'aeiou': # vowel
            # print(i, phrase[i] )
            return i
    return -1
    

lst = [
['apple','pear','kiwi'],
['pizza','msg','salt'],
['cereal','chips','velveeta','cookies']]

'''
make this work:

>>> contains('kiwi',lst)
True
>>> contains('Kiwi',lst)
False
'''
# 2d iteration, search

def contains( target, lst2d ):

    for row in lst2d:
        for item in row:
            if item==target: # found
                return True
    return False

'''
>>> pairsThatAdd( 5, [1,2,3], [4,1,2] )
[(1,4),(3,2)]
'''

def pairsThatAdd( target, numlst1, numlst2 ):

    pairs = []
    for num1 in numlst1:
        for num2 in numlst2:
            if num1+num2 == target:
                pairs.append( (num1, num2) )
    return pairs


treasureMap =\
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~X~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~============~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~====X==============~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~======================~~~~~~~~~~~~~~~~~~
~~~~~~~~=========================~~~~~~~~~~~~~~~~~~~
~~~~~~~~~==========X=========X=======~~~~~~~~~~~~~~~
~~~~~~~~~=========================~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~===================~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~=======================~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~========================~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~=======X==========X==~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~====================~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~==================~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~=================~~~~~~~~~~~~~~~~~~~~~~~
~~~~X~~~~~~~~~============~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

'''
>>> getTreasure( treasureMap )
[(1,4), (3,?), ...]
'''

# 2d indexed accumulator

def getTreasure( tmap ):
    ''' return list of (row,col)
    locations of all treasure (X) on
    tmap'''

    treasure=[]

    tmap = tmap.split()
    for row in range(len(tmap)):
        # print( row, tmap[row] )
        for col in range(len(tmap[row])):
            if tmap[row][col]=='X':
                # print( row, col, tmap[row][col])
                treasure.append( (row, col) )
    return treasure

    




    
            
            












            

            
