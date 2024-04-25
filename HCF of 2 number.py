# a program to calculate hcf of two numbers
x=int(input("enter first number"))
y=int(input("enter the second number"))
if x>y:
    smaller=y
else:
    smaller=x
for i in range(1,smaller+1):
    if((x%i==0)and(y%i==0)):
        hcf=i
print("the HCF of",x,"and",y,"is",hcf)
