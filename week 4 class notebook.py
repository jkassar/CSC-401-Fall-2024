#week 4.py


'''
make this work

>>> oddEven ([22,33,44])
even
odd
even
'''


#print version
def oddEven(numlst):
    for num in numlst:
        #if number is even
        if num%2==0:
            print('Even')
        else:
            print('Odd')


#return version - DOES NOT WORK
#because return stops the loop
def oddEven(numlst):
    for num in numlst:
        #if number is even
        if num%2==0:
            return('Even')
        else:
            return('Odd')



'''
>>> total( [3,12,6,22])
43
'''

#accumulation

def total(numlst):
    #1 - initialize before the loop
    #sum of all the numbers that we have seen
    runningTotal = 0    
    #0 - print version - Iterate through the numbers
    for num in numlst:
        print (num)
        #2 - accumulate in the loop
        #runningTotal = runningTotal + num
        #or
        runningTotal += num
        print(vars())
    #3 return after the loop
    return runningTotal
        

'''
make this work:

>>> countNegs ( [ 2,-5,-23,44,2])
2
'''

def countNegs(numlst):
    #step 1
    count = 0 #count of negative numbers
    #step 0
    for num in numlst:
        if num<0:
            #print(num)
            #step 2
            count+=1
            #count = count+1
    #3
    return count



'''
>>> negatives ([2,-5,-23,44,2])
[-5,-23]
'''

def negatives(numlst):
    #1
    ans = []
    #0
    for num in numlst:
        if num<0:
            #print(num)
            #2
            ans.append(num)
    #3
    return ans



'''
make this work
>>> stripPunct('How, are you?!')
'How are you'
'''

#version 1 - build up one character at a time
def stripPunct(phrase):
    ans = ''
    for char in phrase:
        if char not in '.,;?!;':
            print (char)
            ans+= char
    return ans

#version 2  - same strategy, but using a list, then join - Best for huge data strings
def stripPunct(phrase):
    characters = ''
    for char in phrase:
        if char not in '.,;?!;':
            print (char)
            ans+= char
    return ''.join(characters)

#version 3 - replace one punctuation character at a time
def stripPunct(phrase):
    #iterate over punctuation characters
    for punct in '.,;?!;':
        #replace current punctuation in the string
        phrase = phrase.replace(punct,'')
        #print(phrase)
    return phrase


#search
'''
make this work
>>> hasVowel('hello, how are you?')
true
>>> hasVowel('jfjfjfjfjfjjf')
false
'''

#incorrect, stops after checking the first character
def hasVowel(string):
    for char in string:
        if char in 'aeiou':
            return True
        else:
            return False
        
#search
#correct version - one return in teh loop
#one return after the loop
def hasVowel(string):
    for char in string:
        if char in 'aeiou':
            return True
        #did not find a vowel in the loop
    return False



#accumulator

'''
>>> vowelIndices('hello, how are you')
[1,4,...]
'''
#indexed, accumulator

def vowelIndices(phrase):
    indices = []
    for i in range(len(phrase)):
        #if a vowel
        if phrase[i] in 'aeiou':
            #print (i,phrase[i])
            indices.append(i)
    return indices



'''
>>> firstVowel('hello, how are you')
-1
>>> firstVowel ('jkjkjkjkj')
-1
'''
#indexed search
def firstVowel(phrase):
    for i in range(len(phrase)):
        if phrase[i] in 'aeiou':
            #print(i, phrase[i])
            return i 
    return -1 # vowel not found 


#2-dimentional iteration/nested loop

lst =[
['apple','pear','kiwi'],
['pizza','msg','salt'],
['cereal','chips','velveeta','cookies']]

'''
make this work:

>>> contains('kiwi','lst')
True
>>> contains('Kiwi',lst')
'''

#2d Iteration, search

def contains(target, lst2d):
    for row in lst2d:
        for item in row:
            if item==target:
                return True
    return False        



tmap=\
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~X~~~=======~~~~~~~~~~~~~
~~~~~~~~~~========~~~~~~~~~~~~
~~~~~~~~===========~~~~~~~~~~~
~~~~~~~~====X====X~~~~~~~~~~~~
~~~~~~~~============~~~~~~~~~~
~~~~~~~~==X=========~~~~~~~~~~
~~~~~~~~~=====X===~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~X~~~~~
'''


''' getTreasure(tmap)
[(1,4),...]
'''

#accumulator, 2d, indexed
def getTreasure(tmap):
    '''return list of (row,col) coordinates of all treasure (X) on tmap'''
    treasure=[]
    tmap = tmap.split() # now a list of strings
    for row in range(len(tmap)):
        #print(row, tmap[row])
        for col in range(len(tmap[row])):
            #if treasure
            if tmap[row][col]=="X":
                #print(row, col, tmap[row][col])
                treasure.append((row,col))
    return treasure
