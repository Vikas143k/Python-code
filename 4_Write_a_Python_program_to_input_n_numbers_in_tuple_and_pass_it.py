# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:40:18 2021

@author: writv
"""

#Python program to input n numbers in tuple and pass it to function to count the even and odd numbers are entered.
def countevenodd(arr):
    n=len(arr)
    even=0
    odd=0
    for i in range(n):
        if arr[i]%2==0:
            even=even+1
        else:
            odd=odd+1
    return(even,odd)
arr=[]
n=int(input("Enter no of elements"))
for i in range(n):
    b=int(input("Enter the element"))
    arr.append(b)

t=tuple(arr)
print("Values in the Tuple are: ",t)
e,o=countevenodd(t)
print("Total no of Even numbers",e)
print("Total no of Odd numbers",o)