#Write a Python Program to Find the Largest Number in a List
list=[]
n=int(input("Enter the number of element you want to be in tuple"))
for i in range(n):
    a=int(input("Enter the element"))
    list.append(a)
print(list)
print("largest number in a List", max(list))