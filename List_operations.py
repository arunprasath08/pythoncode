#Pre-defined list
#lst = [12, 5, 8, 19, 3]

#list declaration
lst=list()
# lst=[]

#Getting values from user and appending to list
for x in range(0,6):
    lst.append(int(input("Enter value : ")))
#lst.append(x for x in range (0,3))

# list comprehension
# lst=[int(input(f'Enter values for list element {i+1} : ')) for i in range(6)]

print('Provided list is : ', lst)

print('Maximum value of the list : ', max(lst))

print('Minimum value of the list : ', min(lst))

print('Average value of the list : ', sum(lst)/len(lst))

