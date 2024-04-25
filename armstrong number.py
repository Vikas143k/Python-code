#program to find armstrong number
num=int(input("enter a number"))
sum=0
b=num
while b>0:
    d=b%10
    sum+=d**3
    b//=10
if num==sum:
    print("number is an armstrong number")
else:
    print("not an armstrong number")
