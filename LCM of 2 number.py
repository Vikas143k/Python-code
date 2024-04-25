#python program to find the lcm of 2 numbers
x=int(input("enter the first number"))
y=int(input("enter the second number"))
if x>y:
    greater=x
else:
    greater=y
while(True):
    if((greater%x==0)and(greater%y==0)):
        lcm=greater
        break
    greater+=1
print(lcm)
