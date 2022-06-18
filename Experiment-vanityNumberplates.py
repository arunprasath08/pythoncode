word='AAA33R'
lst=[]

for i in word:
    if i.isnumeric():
        print(i)
        startidx=word.index(i)
        break

lst=word[startidx:]

print(lst)



print(lst.index(lst[0]),lst.index(lst[1]),lst.index(lst[0])==lst.index(lst[1]))

for i in lst:
    print(i,lst.index(i),i.isnumeric())
##    if wrdlst[i].isnumeric():
##        startidx=i
    

#print(idx)
