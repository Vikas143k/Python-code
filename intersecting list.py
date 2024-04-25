#Write a Python Program to Find the Intersection of Two Lists
list1=[]
list2=[]
result=[]
n=int(input("Enter the number of element you want to be in first tuple"))
for i in range(n):
    a=int(input("Enter the element"))
    list1.append(a)
m=int(input("Enter the number of element you want to be in second tuple"))
for i in range(m):
    b=int(input("Enter the element"))
    list2.append(b)
for i in list1:
    for j in list2:
        if i==j:
            result.append(i)
print(result)
