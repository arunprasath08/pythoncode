#to find dupes in a word#
##word='arunprasath'
##c=0
##
##for i in word:
##    for j in word:
##        #print('i=',i,'j=',j)
##        if i==j:
##            c+=1
##    print(i,'is repeated ',c,'times.')
##    c=0

#Result#
##a is repeated  3 times.
##r is repeated  2 times.
##u is repeated  1 times.
##n is repeated  1 times.
##p is repeated  1 times.
##r is repeated  2 times.
##a is repeated  3 times.
##s is repeated  1 times.
##a is repeated  3 times.
##t is repeated  1 times.
##h is repeated  1 times.


#to find dupes in a word-eliminated redundant result of repeating char#
##word='arunprasath'
##c=0
##ref=[]
##
##for i in word:
##    for j in word:
##        #print('i=',i,'j=',j)
##        if i in ref:
##            break
##        else:
##            if i==j:
##                c+=1
##    ref.append(i)
##    print(i,'is repeated ',c,'times.')
##    c=0

#Result#
##a is repeated  3 times.
##r is repeated  2 times.
##u is repeated  1 times.
##n is repeated  1 times.
##p is repeated  1 times.
##r is repeated  0 times.
##a is repeated  0 times.
##s is repeated  1 times.
##a is repeated  0 times.
##t is repeated  1 times.
##h is repeated  1 times.


#to find dupes in a word-managed to get only repeating results#
word=input('Enter some string to check dupes:')
c=0
ref=[]

for i in word:
    for j in word:
        #print('i=',i,'j=',j)
        if i in ref:
            break
        else:
            if i==j:
                c+=1
    ref.append(i)
    if c>1:
##        print('from c>1')
        print(i,'is repeated ',c-1,'times.')
##    else:
##        print('from c not > 1')
##        print(i,'is repeated ',c,'times.')
    c=0
