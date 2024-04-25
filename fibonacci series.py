#Python program to print fibonacci series upto n
n=int(input("Enter the number->>"))
a=1
b=-1
list=[]
for i in range(n):
    a,b=a+b,a
    list.append(a)
print(list)
