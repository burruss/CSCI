#!/usr/bin/env python27

def hello():
    print 'Hello World!'

def printText(text):
    print text

def capitalize(word):
    if isinstance(word, (int)):
        print 'None'

    else:
        letter = word[0].upper()
        print letter + word[1: ]
    
    

def triple(x):
    if isinstance(x,(int,float)):
        print x  * 3

    else:
        print 'None'

def multiply(i,j):
    if isinstance(i, (int,float)) and isinstance(j, (int,float)):
        print i * j
    
    else:
        print 'None'

def printList():
    print '[1, 1.0, \'one\']'



hello()

printText('Greeting World!')

capitalize('bridgewater')

capitalize(10)

triple(10)

triple(3.3)

triple('three')

multiply(2,3)

multiply(1.1,2.2)

multiply(1.1,3)

multiply('one','two')

printList()

print '3'

print '2'

print 'None'

print '2'

print '1'

print 'None'

