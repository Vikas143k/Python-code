#Write a Python Program to Find the Union of two Lists
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
union = list(set().union(list1, list2))

print('The Union of two lists is:', union)
