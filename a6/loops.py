#!/usr/bin/env python27

print "Problem 1"
i = 1
while i < 11:
    print i,
    i += 1
print "\nProblem 2"
i = 10
while i > 0:
    print i,
    i -= 1
print "\nProblem 3"
i = 2
while i < 21:
    print i,
    i +=2
print "\nProblem 4"
i = 1
while i <21:
    print i,
    i += 2
print "\nProblem 5"
i = 3
while i < 20:
    print i,
    i += 3
print "\nProblem 6"

for i in range(1,11):
    print i,
print"\nProblem 7"
for i in reversed(range(1,11)):
    print i,
print "\nProblem 8"
for i in range(0,21,2):
    print i,
print "\nProblem 9"
for i in range(1,20,2):
    print i,
print "\nProblem 10"
for i in range(3,20,3):
    print i,
print "\nProblem 12"
i = "(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)",

print i
print "\nProblem 14"
i = range(1,11)
for x in i:
    if x%2 != 0:
        print '0 ',
    if x%2 != 0:
        print '1 ',
print "\nProblem 16"
i = range(1,6)
for x in i:
    if i[0] == 1:
        print "1 0 0 0 0"
        
        if i[1] ==2:
            print "0 1 0 0 0"
            
            if i[2] == 3:
                print "0 0 1 0 0"
                
                if i[3] == 4:
                    print "0 0 0 1 0"
                    
                    if i[4] == 5:
                        print "0 0 0 0 1"
                        break
