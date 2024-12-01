#Mid Term problems

def coffeePrice(size,adds):
    price = 0
    if size == 'S':
        price +=3.25
    elif size == 'M':
        price += 4.25
    else:
        price += 5.25
    new = adds.split()
    price += (len(new)*0.50)
    return price

def listMax(alpha, beta):
    lst = []
    for i in range(len(alpha)):
        if alpha[i] > beta[i]:
            lst.append(alpha[i])
        else:
            lst.append(beta[i])
    return lst


def hide(phrase):
    ans = ''
    for char in phrase:
        if char in '0123456789':
            ans+= '#'
        else:
            ans += char
    return ans

def getMultiples(target, lst):
    final = []
    for item in lst:
        for j in item:
            if j % target == 0:
                final.append(j)  
    return final



def altcase(word):
    ans = ''
    if i%2 ==0:
        ans += word[i].upper()
    else:
        ans+=word[i].lower()
    return ans

def numCap(phrase):
    lst2 = 0
    lst1 = phrase.split()
    for item in lst1:
        if item[0].isupper():
            lst2+=item
    return lst2
