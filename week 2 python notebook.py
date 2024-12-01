# week2.py

x=2+7

#to display something
print('2+3')


#define a function
   
def myFunction():
    x = 4*3
    print(x)

print("statement not in the function")


#function with parameters

def function(x,y):
    print('x is',x)
    print('y is',y)


'''
make this work
>>>celsius(32.0)
0.0
>>> celsius(212.0)
100.0
>>> celsius(32) - 8.3 #winchill
-8.3
'''
def celsius(f):
    ''' given a farenheight temperature
return the celsius equivalent'''
    c=(f-32)*5/9
    return c

#v1
def votingAge(age):
    '''determines whether a person with given age is old
enough to vote'''
    if age>=18:
        print('You are old enough to vote')
    print('Bye')



#v2 - bad code dont do this
def votingAge(age):
    '''determines whether a person with given age is old
enough to vote'''
    if age>=18:
        print('You are old enough to vote')
    if age<18:
        print('You cannot vote')
        print('wait',18-age,'years')
    print('Bye')


#v3 - the good version
def votingAge(age):
    '''determines whether a person with given age is old
enough to vote'''
    if age>=18:
        print('You are old enough to vote')
    else:
        print('You cannot vote')
        print('wait',18-age,'years')
    print('Bye')


'''
>>> say('hello',3)
hello
hello
hello
>>> say('bye',2)
bye
bye
>>>say ("ohmygosh!',0)
>>>
'''

def say(word,n):

    for i in range(n):
        print(word)


'''
make this work:
>>> lst = ['apple','hello', 'pear','orange']
>>vowelStart (lst)
apple
orange
'''

def vowelStart(wordlst):
    for word in wordlst:
        #if word begins with vowel
        if word[0] in 'aeiouAEIOU':
            print(word)






def maximum(num1,num2):
    if num1>=num2:
        print(num1)
    else :
        print(num2)



