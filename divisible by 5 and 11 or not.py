#a python program to check whether a number is divisible by 5 and 11 or not.
n=int(input("Enter the Number->"))
if n%5==0 and n%11==0:
    print(f"{n} is divisible by 5 and 11")
else:
    print(f"{n} is not divisible by 5 and 11")