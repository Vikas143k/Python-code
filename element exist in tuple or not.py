#Python program to check whether an element exists within a tuple
tuple1=(1,2,3,4,5,6,7,8,9,10,10)
n=int(input("Enter the number you what to find if that exist within in the tuple or not-> "))
a=0
for i in tuple1:
    if n==i:
        print("The element exists in the tuple")
        a+=1
        break
if a==0:
    print("The element does not exist in the tuple")
