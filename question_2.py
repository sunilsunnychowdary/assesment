arr=[1,2,8,10,11,12,8,2,54,10]
arr.sort()
j=0
temp=[]
for i in range(0,len(arr)-1):
    if(arr[i]!=arr[i+1]):
        temp.insert(j,arr[i])
        j=j+1
temp.insert(j+1,arr[len(arr)-1])
for k in range(0,j+1):
    print(temp[k])
