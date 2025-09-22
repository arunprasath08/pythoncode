##list=[1,1,2,3,5,4,3,2]
##repeat=[]
##no_repeat=[]
####for i in list:
####    print('i:',i)
####    for j in list[:]:
####        print('j:',j)
####        if i!=j:
####            print(j,'is available')
##
##for i in range(len(list)):
##    if (list[i] in list[i+1:]) and list[i] not in repeat:
##        repeat.append(list[i])
##    elif (list[i] not in list[i+1:]) and list[i] not in repeat:
##        no_repeat.append(list[i])
##
##print('repeated elements list:',repeat)
##
##print('Not repeated elements list:',no_repeat)


string='arunprasath'
repeat=[]
no_repeat=[]
##for i in list:
##    print('i:',i)
##    for j in list[:]:
##        print('j:',j)
##        if i!=j:
##            print(j,'is available')

string_rep_list=[string[i] for i in range(len(string)) if (string[i] in string[i+1:]) and (string[i] not in string[:i])]

print(string_rep_list)
print(''.join(string_rep_list))

string_not_rep_list=[string[i] for i in range(len(string)) if (string[i] not in string[i+1:]) and (string[i] not in string[:i])]

print(string_not_rep_list)
print(''.join(string_not_rep_list))


#print('repeated elements list:',repeat)

#print('Not repeated elements list:',no_repeat)
