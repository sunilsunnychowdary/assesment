arr=[]
for j in range(0,100):
    arr.insert(j,j+1)

n=int(input("enter number to delete"))
for k in range(0,100):
    if arr[k]==n:
        del arr[k]
        break
    
for i in range(1,101):
     if i not in arr:
         print(i)


    
