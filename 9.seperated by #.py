# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:03:10 2021

@author: writv
"""

# Program to read a text file line by line and display each word 
# separated by a #.
f=open("school.txt","w")
f.write("My School\n")
f.write("My School name is Kendriya Vidyalaya\n")
f.write("It is situated in Siddartha Nagar Mysuru")
f.close()

fin=open("school.txt","r")
ctr=fin.read()
print(ctr)
fin.close()
print("The Result is:")
filein = open("school.txt",'r')
for  line in filein:
     word= line .split()
     for w in word:
          print(w,end ='#')
filein.close()
