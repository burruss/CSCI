#!/usr/bin/env python27

print 'Problem 1'
print '\t',
i = 6
while i < 20:
    if i % 6 ==0:
        print i,
        i += 6

print '\nProblem 2'
print '\t',
i = 1

while i < 101:
    if (i % 5 == 0) and (i % 6 == 0):
        print i,
    i += 1

print '\nProblem 3'
print '\t',
i = 97

while i < 123:
    print chr(i),
    i += 1

print '\nProblem 4'
print '\t',
i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for x in i:
    while x % 6 == 0:
        print x,
        x += 1        

print '\nProblem 5'
print '\t',

for x in range(1,101):
    if (x % 5 == 0 and x % 6 == 0):
        print x,

print '\nProblem 6'
print '\t',

for i in range(97,123):
    print chr(i),


print '\nProblem 8'
print '\t',

for i in range(1,101):
    if (i % 2 == 0 and i % 6 == 0):
        print i,

print '\nProblem 10'
print '\t',

for i in range(1,101):
    if (i % 6 == 0):
        print i,


print '\nProblem 12'
print '\t',
x = [1, 2, 3, 4, 5]

for i in x:
    if i <= 5:
        print 'o',
        
        if  i > 5:
            print '\n'
            if i < 2:
                print 'o',
                if i <= 4:
                    print 'x',
                    if i == 5:
                        print 'o',
