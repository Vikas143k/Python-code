#Python Program to Find the Factorial of a Number
import math
n=int(input("Enter the number to find the factorial "))
if n>0 or n==0:
    b=math.factorial(n)
    print(f"Factorial of {n} is {b}")
else:
    print("Factorial doesn't exist")
