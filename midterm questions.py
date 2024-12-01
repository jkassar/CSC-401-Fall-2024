#practice questions



# 4.17


#a
def f(phrase):
    alpha=phrase.split()
    beta = len(alpha)
    charlie = alpha.count('secret')
    #return c 
    delta = phrase.replace('secret','xxxxxx')
    return delta


#4.18

def story(phrase):
    newS = phrase.replace('.','').replace(',','').replace(';','').replace('\n','')
    #print (newS)
    newS = newS.lower
    #print (newS.count('it was'))
    newS = newS.split().replace('was','is')
    listS = newS.split()
    print (listS)



    
#4.19

def alpha (first, last, middle):
    beta = f'''{last}, {first} {middle}'''
    return beta
def delta(first, last, middle):
    epsilon = middle[0]
    gamma = f'''{last}, {first} {epsilon}.'''
    return gamma

def sigma(first, last, middle):
    rho = middle[0]
    zeta = f'''{first} {rho}. {last}''' 
    return zeta



#4.20







def gct(tbsp):
    gal = tbsp//256
    tbsp2 = tbsp%256
    cup = tbsp2//16
    tbsp3 = tbsp2%16
    return f'''{gal}g,{cup}c,{tbsp3}t'''












    
