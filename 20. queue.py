# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:33:08 2021

@author: writv
"""

#WAP to perform enqueue and dequeue operation in a queue
q=[]
choice='y'
while choice=='y' or choice=='Y':
           print("Option Menu")
           print("----------------------------------------------")
           print("1. Enqueue (Insert) an Element in Queue")
           print("2. Dequeue (Delete) an Element from Queue")
           print("3. Traverse (Display) Queue Data")
           print("----------------------X------------------------")
           opt=int(input("Enter your choice from above Menu (1,2 or 3) :"))
           if (opt==1):
                      d=input("Enter the data to be inserted in Queue")
                      q.append(d)
           elif (opt==2):
                      if (q==[]):
                                 print("Queue is Empty")
                      else:
                                 p=q.pop(0)
                                 print("Deleted ",p,"from Queue")
           elif (opt==3):
                      l=len(q)
                      for i in range (0,l):
                                 print(q[i])
           else:
                      print("Invalid Option")
           choice=input("Do you want to continue (y or n): ")
