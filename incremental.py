n=1

def inc(a):
    val=a*a
    print('iteration ',a,'is',val)
    return val

inc(n)

m=n+1
print('n is',n,'and m is',m)

# while(m>1):
#     inc(m)
for i in range(10):
    c=inc(m)
    m=c

