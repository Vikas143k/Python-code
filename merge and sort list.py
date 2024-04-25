#Write a Python Program to Merge Two Lists and Sort it
list1=[]
list2=[]
n=int(input("Enter the number of element you want to be in first tuple"))
for i in range(n):
    a=int(input("Enter the element"))
    list1.append(a)
m=int(input("Enter the number of element you want to be in second tuple"))
for i in range(m):
    b=int(input("Enter the element"))
    list2.append(b)
print(list1)
print(list2)
a=list1+list2
a.sort()
print("merged tuple after sorting",a)