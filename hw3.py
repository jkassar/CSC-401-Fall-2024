# hw3.py
# Name: Jumana Kassar
# Collaborators: Abdul Momin, Shivani Chopra
# References:

#4.24 - DONE

def cheer(name):
    print ('How do you spell winner?\nI know, I know!')
    caps = name.upper()
    let= ''
    for i in caps:
        let+=i +' '
    print(let+'!')  
    letter = (f'''And that's how you spell winner!\nGo {name}!''')
    print (letter.format(name))

#4.25 - DONE

def vowelCount (phrase):
    for char in phrase:
        acount = phrase.count('a')
        ecount = phrase.count('e')
        icount = phrase.count('i')
        ocount = phrase.count('o')
        ucount = phrase.count('u')
    letter = '''a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {} times.'''
    print (letter.format(acount,ecount,icount,ocount,ucount))
        

#4.26 DONE
 
def crypto(file):
    infile = open(file, 'r')
    lineList = infile.read()
    public = lineList.replace('secret','xxxxxx')
    print(public)

#4.28 DONE 

def links(htmlfile):
    file = open(htmlfile)
    content = file.readlines()
    hyperlinks_count = 0
    for hyperlinks in content:
        hyperlinks_count += hyperlinks.count('</a>')
    return hyperlinks_count


#4.31 DONE

def duplicate(filename):
    infile = open(filename)
    contents= infile.read()
    infile.close()
    StepOne = contents.replace('.','').replace(',','').replace('?', '')
    StepTwo = StepOne.lower().split()
    for i in range(len(StepTwo)):
        for j in range(i+1, len(StepTwo)):
        # compare current word to words that come after to see if any match
            if StepTwo[i] == StepTwo[j]:
                return True
    return False #returns after checking all words

#doctest
if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw3TEST.py'))

