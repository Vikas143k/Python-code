# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:42:15 2021

@author: writv
"""

# Storing capital and currency of countries and searching particular country
d1=dict()
i=1
n=int(input("enter number of entries"))
while i<=n:
    c=input("enter country")
    cap=input("enter capital:")
    curr=input("enter currency of country")
    d1[c]=(cap,curr)
    i+=1
print(d1)
l=d1.keys()
print("\nCountry\t\t","Capital\t\t","currency")
for i in l:
    z=d1[i]
    print('\n',i,"\t\t",end="")
    for j in z:
        print(j,"\t\t",end="\t\t")
x=input("\nEnter country to be searched")
for i in l:
    if i==x:
        print("\nCountry\t\t","Capital\t\t","currency\t\t")
        z=d1[i]
        print('\n',i,"\t\t",end="")
        for j in z:
            print(j,"\t\t",end="\t\t")
        break
else:
    print("country not found")