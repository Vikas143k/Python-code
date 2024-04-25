#Write a Python program to count number of digits in a number
n=int(input("Enter the number"))
b=n
a=0
while True:
    if n!=0:
        a+=1
        n//=10
    else:
        break
print(f"digit in {b}->{a}")

