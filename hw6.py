#HW6
#Name - Jumana Kassar
#Collaborators - Shivani Chopra and Abdul Momin


#interleaved
def interleaved(lstA, lstB):
    lstC = []
    i, j = 0, 0
    while i < len(lstA) or j < len(lstB):
        if i < len(lstA) and (j >= len(lstB) or lstA[i] <= lstB[j]):
            lstC.append(lstA[i])
            i += 1
        elif j < len(lstB):
            lstC.append(lstB[j])
            j += 1

    return lstC

#primeFac

def primeFac(num):
  factor = []
  candidate = 2
  while num>1:
    if num%candidate==0:
      factor.append(candidate)
      num //= candidate
    else:
      candidate += 1
  return factor
   
    

#piggyBank

def piggyBank(lst1):
  d = {'Q':0, 'D':0, 'N':0,'P':0 }
  for i in lst1:
    d [i] += 1
  p = (d['Q']*25)+(d['D']*10)+(d['N']*5)+(d['P']*1)
  return d, p


#craps
import random

def craps():
    def roll_dice():
        return random.randrange(1, 7) + random.randrange(1, 7)
    initial_total = roll_dice()
    if initial_total in [7, 11]:
        return 1
    elif initial_total in [2, 3, 12]:
        return 0
    point = initial_total
    while True:
        new_total = roll_dice()
        
        if new_total == point:
            return 1 
        elif new_total == 7:
            return 0 




#testCraps
import random
def testCraps(n):
  points = 0
  for i in range(n):
    result = craps()
    if result == 1:
      points +=1
  return points/n



if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw6TEST.py'))

