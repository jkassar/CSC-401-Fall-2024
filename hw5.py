# hw5
# Name: Jumana Kassar
# Collaborators: Abdul Momin, Shivani Chopra
# References

# doubleVowel

def doubleVowel(phrase):
    for i in range(len(phrase)-1):
        if phrase[i] in 'aeiouAEIOU' and phrase[i+1] in 'aeiouAEIOU':
            return True  
    return False
        

# numPairs

def numPairs(target, lst1):
    ans = 0
    for i in range(len(lst1)):
        for j in range(i + 1, len(lst1)):  
            if lst1[i] + lst1[j] == target:
                ans += 1
    return ans


# hideShow

def hideShow(instg, mskstg):
    ans=''
    for i in range(len(mskstg)):
        if mskstg[i]=='0':
            ans += '#'
        else:
            ans+= instg[i]
    return ans
  

# clean

def clean(string):
    start = 0
    while start < len(string) and string[start] == ' ' or string[start] == '\n' or string[start]== '\t':
        start += 1
    end = len(string) - 1
    while end >= 0 and string[end] == ' ' or string[end] == '\n' or string[end]== '\t':
        end -= 1
    return string[start:end + 1]

# sequence

def sequence(n):
    while n != 1:  
        print(n)   
        if n % 2 == 0:  
            n //= 2     
        else:           
            n += 1
    print(1)


if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py'))


