#Write a Python program to test whether a number is within 100 or 1000 or 2000.
n=int(input("Enter the number"))
if n<100:
    print(f"{n} is within 100")
elif n>99 and n<1000:
    print(f"{n} is within 1000")
elif n<2000 and n>999:
    print(f"{n} is within 2000")
else:
    print("it's beyond or equals to 2000")