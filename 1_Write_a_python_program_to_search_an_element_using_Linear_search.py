def linser(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

arr=[]
n=int (input ("Enter no of elements to add to the list"))
for i in range(n):
    b=int(input ("Enter the element :"))
    arr.append(b)
print ("List entered is: ",arr)
x=int (input ("Enter the number you want to search: "))
pos=linser(arr,x)
if pos==-1:
    print ("Element not found") 
else:
    print ("Element found at position", pos+1)