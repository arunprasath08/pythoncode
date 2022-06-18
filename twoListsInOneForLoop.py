list1=[1,2,3,4,5,6,7,8,9,0]
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']

'''Prints values corresponding to length of one of the list, 
in this case only 5 elements from each list'''
# for i in zip(list1,list2):
#     print(list1[i],list2[i])

'''Prints values corresponding to length of list with max length, 
in this case all elements from each list printed'''
def print_list(list_obj,pos):
    try:
        print(list_obj[pos],'\t',end='')
    except:
        print(' \t',end='')
    else:
        return

for i in range(max(len(list1),len(list2))):
    print_list(list1,i)
    print_list(list2,i)
    print('\n')

