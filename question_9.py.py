 
def bubbleSort(mylist):
    n = len(mylist)
  
    for i in range(n-1):
  
        for j in range(0, n-i-1):

            if mylist[j] > mylist[j+1] :
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
  
n=int(input("enter the number of elements to be inserted:"))
print("enter the elements:\n")
mylist=[]
for j in range(n):
    k=int(input())
    mylist.append(k)
bubbleSort(mylist)
  
print ("Sorted list is:")
for i in range(len(mylist)):
    print (mylist[i])