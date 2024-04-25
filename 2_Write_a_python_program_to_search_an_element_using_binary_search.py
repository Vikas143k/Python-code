# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:38:35 2021

@author: writv
"""

def binary_search(a,key):
    start=0
    end=len(a)-1    
    while start<=end:
        mid=int((start+end)/2)
        if a[mid]>key:
            end=mid-1
        elif a[mid]<key:
            start=mid+1
        else:
            return mid+1
m=[]
n=int(input("Enter no of elements"))
for i in range(n):
    b=int(input("Enter the element"))
    m.append(b)
a=sorted(m)
k=int(input("enter the number to be found"))
print("element found at",binary_search(a,k))