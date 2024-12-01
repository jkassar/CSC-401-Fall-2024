def numCapitalized(phrase):
    lst2 = 0
    lst1 = phrase.split()
    for item in lst1:
        if item [0].isupper():
            lst2+= 1
    return lst2



def priceTShirt(size,phrase):
    price = 0
    if size =="S":
        price += 12
    elif size == 'M':
        price += 15
    elif size == 'L':
        price += 18
    for i in phrase:
        if i in ' .,!\'\"?:':
            price +=0.2
        elif i.isupper():
            price +=0.30
        elif i.islower():
            price +=0.25
        else:
            price += 0
    return price

def alterCase(phrase):
    new = []
    for char in phrase[0::2]:
        if phrase[char]%2 ==0:
            new += char

    return new 




def f(n):
    i = 0
    while n>0:
        n-=3
        i+=1
    return i


    





