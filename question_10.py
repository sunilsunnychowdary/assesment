def mergeSort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]

        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              mylist[k] = left[i]
              i += 1
            else:
                mylist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mylist[k]=right[j]
            j += 1
            k += 1

 
n=int(input("enter the number of elements to be inserted:"))
print("enter the elements:\n")
mylist=[]
for j in range(n):
    k=int(input())
    mylist.append(k)
mergeSort(mylist)
print("sorted elements are:\n")
for i in range(len(mylist)):
    print(mylist[i])
