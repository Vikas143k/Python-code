#Write a Python Program to Put Even and Odd elements in a List into Two Different Lists
list=[]
even=[]
odd=[]
n=int(input("Enter the number of element you want to be in tuple"))
for i in range(n):
    a=int(input("Enter the element"))
    list.append(a)
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even tuple:-",even )
print("odd tuple:-",odd)