# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:39:34 2021

@author: writv
"""

def change (arr):
    n=len(arr)
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=arr[i]/2
        else:
            arr [i]=arr[i]*2
arr=[]
n=int (input ("Enter no of elements"))
for i in range(n):
    b=int (input ("Enter the element"))
    arr.append (b)
print ("Original List if: ",arr)
change(arr)
print ("List After Change ",arr)