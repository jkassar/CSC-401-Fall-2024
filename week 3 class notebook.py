

#v1 = bad because it doesnt convert to numbers
def inputTest(): #no parameters, gets data from user instead
    number = input('Enter a number: ')
    print("Your number is", number)
    print("Twice your number is",2*number)
    
#v2 - better
def inputTest(): #no parameters, gets data from user instead
    number = eval(input('Enter a number: '))
    print("Your number is", number)
    print("Twice your number is",2*number)


'''
make this work:

>>> numchars('out.txt')
???
'''

#v1 - Proper, but verbose

def numchars(filename):
    #open the file
    infile = open(filename)
    
    #read contents
    infile.read()
    
    #close the file
    contents = infile.close()

    #count the characters and return
    return len(contents)


#v2 - very succinct, but can't close the file
def numchars(filename):
    return len(open(filename).read())

#v3 - use with a compromise
def numchars(filename):
    with open(filename) as infile: #infile = open(file name)
        return len(infile.read())
    #with guarantees that the file








'''Make this work:

>>>getCell(1,2,'numbers.csv')

-7
'''


def getCell(rowIndex,colIndex,filename):
    
    ''' return number from csv filename at location
rowIndex colIndex using python (using 0-base Python coutnting)'''
    with open(filename) as csvfile:
        return eval (csvfile.readlines()[rowIndex].split(',')[colIndex])



#shoulda been in week 2

'''
want this to work
>>> status (67.3) # temperature farenheit
'warm'
>>> status(30)
'cool'
>>>status (-13.2)
'cold'
>>> status(99)
'hot'

'''
#shouldnt do this , right but not good style
def status(temp):
    '''return status hot/warm/cool/cold of given farenheit temp'''
    if temp>=80:
        return 'hot'
    elif temp<80 and temp>=50:
        return 'warm'
    elif temp<50 and temp>=10:
        return 'cool'
    else:
        return 'cold'


#do this instead
def status(temp):
    '''return status hot/warm/cool/cold of given farenheit temp'''
    if temp>=80:
        return 'hot'
    elif temp>=50:
        return 'warm'
    elif temp>=10:
        return 'cool'
    else:
        return 'cold'

