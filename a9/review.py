#!/usr/bin/env python27

# 1 mv py a7

# 2 chmod 700 py

# 3 git add file1.py
#   git comit -m ""
#   git push

# #!/usr/bin/env python27

def isOdd(x):
    if isinstance(x,int or float or long):
        if x % 2 != 0:
            print 'true'
        else:
            print 'false'

isOdd(6)

def reverseString(i):
    if isinstance(i, str):
        print i[::-1]
    else:
        print 'None'

reverseString(16)

def equalLists(i,j):
    if isinstance(i,list) and isinstance(j,list):
        if i == j:
            print 'true'
    else:
        print 'false'

equalLists([1,2,3],[1,2,3])

def cloneList(i):
    if isinstance(i,list):
        j = i
        print j
    else:
        print 'None'

cloneList([1,'a',3])

def init2DArray(x):
    if isinstance(x,int):
        L = []
        for i in range(x):
            L.append([])
            for j in range(x):
                if (i+1) * (j+1) == ((i+1) * (i+1)):
                    L[i].append(1)
                else:
                    L[i].append(0)

    for i in range(x):
        
        for j in range(x):
            print L[i][j],
        print ''
    print''

init2DArray(4)
                
