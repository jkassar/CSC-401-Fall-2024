# week 7


'''
frequencies([5,8,5,8,7])
{5:2, 8:2, 7:1}

'''


#accumulate a dict

def frequencies (iterable):
    #create an empty dictionary
    counts = {}
    #iterate over the iterable
    for item in iterable:
        #if a new item, add key with count of 1
        if item not in counts:
            counts[item]=1
        # old item, increase count by 1
        else:
            counts[item] += 1
    #return dictionary
    return counts 



#roll a dice
'''
diceTotal()
(19)
'''

import random
def diceTotal():
    pips = 0

    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    #print (die1,die2)
    pips += die1+die2

    while die1 == die2:
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        #print (die1,die2)
        pips += die1+die2

    return pips







#substitution cypher
'''
make this work
>>> d = {'a':'k', 'b':'g'}
>>> encode('bat',d)
'gkt'
'''

def encode(phrase,d):
    #accumulate a string
    ans = ''
    #iterate over the phrase
    for char in phrase:
        #if letter is dictionary
        if char in d:
            ans += d[char]
        #replace with its value
        else:
            ans += char
        #otherwise use it unchanged
    return ans



'''
decode('gri fhtwm kiq soe uhlxiq onik gri jacv ykozp qod')
'the quick red fox jumped over the lazy brown dog'

'''
msg = msg.upper()
code = {'l':'e','x':'t'}

print(encode(msg,code))
        
