arr=[80,20,30,15,70,5,1]
sort_arr=[]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            tem=arr[i]
            arr[i]=arr[j]
            arr[j]=tem
print(arr)

##arr.sort()
##arr.reverse()
##print(arr)
##for i in range(len(arr)):
##    print(arr[i])

