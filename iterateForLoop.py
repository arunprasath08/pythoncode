num=8148616735
number=str(8148616735)
q_ls=[]
r_ls=[]

l=len(str(num))

for i in range(l):
    q_ls.append(num//10)
    r_ls.insert(i,num%10)
    print(i,l-i,num%10)
    num=q_ls[i]

##q_ls=[num//10 for i in range(len(str(num))) if len(str(num))!=0 num=num//10]
##r_ls=[num%10 for i in range(len(str(num))) if len(str(num))!=0 num=num//10]
##
r_ls.reverse()
print(q_ls,r_ls,sep='\n')

#print(num//10)
#print(num%10)

i=4
for string in range(len(number)):
    if string==i:
        print (str(number[i-1]))
