# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:49:13 2021

@author: writv
"""

# Menu driven proram to find factorial, check prime and reverse a number
def fact():
    # Funtion to find the factorial of a number provided by the user.
    num = int(input("Enter a number:"))
    factorial = 1
    if num<0:
        print("Sorry, factorial does not exist for negative number:" )
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)
def prime():
# Funtionj to check if a number is prime or not
    num=int(input("Enter a number:"))
    if num==2:
        print("2 is a prime number")
    if num>=1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
                break
 
def rev():
    # Function to reverse the entered number
    num = int(input("Enter a number:"))
    rev = 0
    while num>0:
        remainder=num % 10
        rev=(rev*10)+remainder
        num = num//10
    print("The reversed number is :",rev)
while True:
    print("\n Choose Options To Perform :")
    print("1. Factorial of a number")
    print("2. Check the the no is prime or not")
    print("3. Reverse the number")
    print("4. Exit")
    choice =int(input("Enter Your Choice :"))
    if choice==1 :
        fact()
    elif choice==2 :
        prime()
    elif choice==3 :
        rev()
    elif choice==4:
        break
    else :
        print("Invalid Choice")