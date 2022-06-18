#and plate[len(plate)-1:].isalpha()

def main():
    plate=input('Plate:').strip()
    #print(plate[len(plate)-1:])
    #print(len(plate))
    #print(plate[0:2],plate[0:2].isalpha())
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def number_check(n):
    num=[]
    for i in n:
        if i.isnumeric():
            startidx=n.index(i)
            break
    num=n[startidx:]
    #print(num,num[0],type(num[0]))
    if int(num[0])==0:
        #print('inside num[0]==0')
        return False
    elif int(num[0])!=0:
        #print('inside num[0]!=0')
        for i in num:
            #print('printing i before alpha check',i)
            if i.isalpha():
                #print('printing i from inside alpha check',i)
                return False
            else:
                continue
        return True
    else:
        return True

def is_valid(s):
    #print(s,'inside func')
    #print(len(s))
    if len(s)>=2 and len(s)<=6:
        #print(s,'inside first if')
        if s[0:].isalpha():
            return True
        elif s[0:2].isalpha() and s[2:].isalnum():
            #print(s,'inside second if')
            #print(s[0:2])
            num_chk_stat=number_check(s[2:])
            #print('return value from number_check()',num_chk_stat)
            if num_chk_stat==True: 
                return True
            else:
                return False           
        else:
            return False
    else:
        return False


if __name__=='__main__':
    main()
