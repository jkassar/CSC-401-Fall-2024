x = []
for i in range(2):
    for c in 'ab':
        x.append( (i,c) )




x = 175.0
while (x>1):
    x = x/10
print( x )




def f(n):
    i = 0
    while n>0:
        n-=3
        i+=1
    return i



d = {}
d['apple'] = 1.5
print( d, 1.5 in d)
