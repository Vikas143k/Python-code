# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:29:57 2021

@author: writv
"""

#WAP to perform push and pop operation in a stack
s=[]
choice='y'
while choice=='y' or choice=='Y':
           print("Option Menu")
           print("----------------------------------------------")
           print("1. Push (Insert) an Element in Stack")
           print("2. Pop (Delete) an Element from Stack")
           print("3. Traverse (Display) Stack Data")
           print("----------------------X------------------------")
           opt=int(input("Enter your choice from above Menu (1,2 or 3) :"))
           if (opt==1):
                      d=input("Enter the data to be inserted in Stack")
                      s.append(d)
           elif (opt==2):
                      if (s==[]):
                                 print("Stack is Empty")
                      else:
                                 p=s.pop()
                                 print("Popped",p,"from Stack")
           elif (opt==3):
                      l=len(s)
                      for i in range (l-1,-1,-1):
                                 print(s[i])
           else:
                      print("Invalid Option")
           choice=input("Do you want to continue (y or n): ")
