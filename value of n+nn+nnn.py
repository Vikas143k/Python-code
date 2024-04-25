#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
n=int(input("Enter the number"))
a=n+(n*n)+(n**3)
print(f"The value is {a}")