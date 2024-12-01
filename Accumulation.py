# Accumulation.py

##### accumulator pattern #####
'''
A PATTERN is a strategy that applies to
multiple programming problems.

The ACCUMULATOR pattern computes a value
(or fills a container) by  maintaining a
partial/running value through each
iteration of a loop.

EXAMPLES:
    sum, product, count, max, min
    return multiple items, list, str

FOUR STEPS:
0) set up iteration, vist all items
   of interest (write "print" version)
1) initialize running value before loop
2) accumulate in the loop
3) return after loop

TIP: a VARIABLE is a COMMITMENT to keep
track of a piece of information.

(see also list comprehensions/generators )
'''

##### PROBLEM: print vs return #####
'''
make this work:
>>> oddEven( [22,33,44] )
even
odd
even
'''

def oddEven( numlst ):
    for num in numlst:
        if num%2==0: # even
            print('even')
        else:
            print('odd')

#Q: can we return?
#A: NO, return TERMINATES the function/loop

def oddEven( numlst ):
    for num in numlst:
        if num%2==0: # even
            return 'even'
        else:
            return 'odd'
            

##### accumulator #####
'''
make this work:
>>> total( [3,12,6,22] )
43

running total: running total: 0
+3 -> 3
+12 -> 15
+ 6 -> 21
+22 -> 43
'''

# TIP: a VARIABLE is a COMMITMENT

def total( numlst ):
    #1 - initialize accumulator
    runningTotal = 0
    #0 - print version
    for num in numlst:
        #print( num )
        #2 - accumulate
        runningTotal += num
        #runningTotal = runningTotal + num
        #print( vars() )
    return runningTotal
        
        
##### aside: <op>= shorthand #####
'''
<var> <op>= <expr>

is shorthand for

<var> = <var> <op> <expr>

>>> x = 7
>>> x = x + 3
>>> x
10
>>> # shorthand
>>> x += 3
>>> x
13
>>> x+=5
>>> x
18
>>> x*=2
>>> x
36
>>> x -=12
>>> x
24
>>> x //=2
>>> x
12
>>> x %=7
>>> x
5
>>> 

In Java, C, C++, the following are
all equivalent

c = c + 1
c += 1
c++ <- not in Python
'''

##### counting #####
'''
make this work:
>>> countNegs( [2,-55,-23,44,2] )
2

count: 
'''

def countNegs( numlst ):

    # 1
    count = 0
    # 0
    for num in numlst:
        if num<0:
            # 2 
            count += 1
            #print( num )
    # 3
    return count

##### collecting #####
'''
>>> negatives( [2,-55,-23,44,2] )
[-55, -23] <- return a list
'''

def negatives( numlst ):
    # 1
    ans = []
    # 0
    for num in numlst:
        if num<0:
            # 2
            ans.append( num )
            # print( num )
    # 3
    return ans


##### accumulate str #####
'''
make this work:
>>> stripPunct( "How, are, you?!." )
'How are you'
>>>
'''

def stripPunct( phrase ):

    ans = ''
    for char in phrase:
        if char not in '.,!?;:':
            ans += char
            #print( char )
    return ans

# OR, another way
# which is BETTER/FASTER

def stripPunct( phrase ):

    for punct in '.,?;:!':
        phrase = phrase.replace(punct,'')
    return phrase

# write code that WORKS and you know WHY
# it works. Then worry about EFFICIENCY.















