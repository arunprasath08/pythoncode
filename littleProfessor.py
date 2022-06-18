import random as rd
import sys

first_list=[]
second_list=[]
#first_list=rd.sample(range(0,10),10)
#second_list=rd.sample(range(0,10),10)
# first=0
# second=0

def main():
    level=get_level()
    sc=0
    for i in range(10):
        point=0
        a,b=generate_integer(level)
        calc_res=a+b
        res_cnt=3
        while True:
            try:
                while res_cnt>=1:
                    usr_res=int(input('{} + {} = '.format(a,b)))
                    if usr_res!=calc_res and res_cnt!=1:
                        print('EEE')
                        res_cnt-=1
                    elif usr_res!=calc_res and res_cnt==1:
                        print('EEE')
                        print('{} + {} = {}'.format(a,b,calc_res))
                        #point-=1
                        break
                    elif usr_res==calc_res:
                        point+=1
                        #return point
                        break
                    else:
                        pass
            except ValueError:
                if res_cnt==1:
                    print('EEE')
                    print('{} + {} = {}'.format(a,b,calc_res))
                    #point-=1
                    break
                else:
                    print('EEE')
                    res_cnt-=1
            else:
                break
        sc+=point
    return sc

def get_level():
    while True:
        try:
            lev=int(input('Level: '))
            if lev in [1,2,3]:
                return lev
            else:
                continue
        except ValueError:
            continue

def random_generator(start,stop):
    while True:
        first=rd.randrange(start,stop)
        second=rd.randrange(start,stop)
        if first not in first_list or second not in second_list:
            first_list.append(first)
            second_list.append(second)
            #print(first,second)
            return first,second
        else:
            continue

def random_generator_sample():
    a=first_list.pop()
    b=second_list.pop()
    return a,b

def generate_integer(level):
    if level==1:
        start_rang=0
        stop_rang=9
        #a,b=random_generator_sample()
        #a,b=random_generator(start_rang,stop_rang)
        # a=rd.choices((0,1,2,3,4,5,6,7,8,9))
        # b=rd.choices((0,1,2,3,4,5,6,7,8,9))
        # a=rd.randrange(start_rang,stop_rang)
        # b=rd.randrange(start_rang,stop_rang)
        a=rd.randint(start_rang,stop_rang)
        b=rd.randint(start_rang,stop_rang)
        return a,b
    else:
        start_rang=10**(level-1)
        stop_rang=(10**level)-1
        a=rd.randint(start_rang,stop_rang)
        b=rd.randint(start_rang,stop_rang)
        return a,b

if __name__ == "__main__":
    score=main()
    print('Score:',score)
    #random_generator_sample()
