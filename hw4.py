# hw 4
# Name: Jumana Kassar
# Collaborators:Annette Banquells,Shivani Chopra
# References:
#   is_integer function: https://tinyurl.com/4rsmrfea
#   islower/isupper function: https://tinyurl.com/32uchcj8

#vowelIndex 

def vowelIndex (word):
    for i in range(len(word)):
        if word[i] in 'aeiouAEIOU':
            return i
    return -1

#flipCase 

def flipCase(string):
    newstring = ''
    for char in string:
        if char.isupper():
            newstring +=char.lower()
        elif char.islower():
            newstring += char.upper()
    return newstring

#palindromes

def palindromes(phrase):
    lst2= []
    lst1 = phrase.replace('.','').replace(',','').replace('?', '').replace('!', '').split()
    for word in lst1:
        if word.lower()[0:]== word.lower()[::-1]:
            lst2.append(word)
    return lst2


#squares

def squares(strings):
    lst2 = 0
    for x in strings:
        for i in x:
            if (i**.5).is_integer()== True:
                lst2 += 1
    return lst2


#rps

def rps(p1,p2):
    if p1+p2== 'RP':
        return 1
    elif p1+p2== 'RS':
        return -1    
    elif p1+p2== 'SP':
        return -1    
    elif p1+p2== 'SR':
        return 1
    elif p1+p2== 'PR':
        return -1    
    elif p1+p2== 'PS':
        return 1
    else:
        return 0

if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw4TEST.py'))


