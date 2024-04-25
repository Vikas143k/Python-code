# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:58:58 2021

@author: writv
"""

# Program to count Total no of characters, words and lines in a text file

# Writing to text file 
f=open("school.txt","w")
f.write("My School\n")
f.write("My School name is Kendriya Vidyalaya\n")
f.write("It is situated in Siddartha Nagar, Mysuru")
f.close()

# Display from text file
fin=open("school.txt","r")
ctr=fin.read()
print(ctr)
fin.close()

def countchar():        # Counting no of Characters
    fin=open("school.txt","r")
    ctr=fin.read()
    count=0
    for i in ctr:
        count=count+1
    print("Total no of characters",count)
    fin.close()

def countword():        # Counting no of Words
    fin=open("school.txt",'r')
    str=fin.read( )
    L=str.split()
    count_words=0
    for i in L:
        count_words=count_words+1
    print("Total no of words", count_words)
    fin.close()

def countline():        # Counting no of Lines
    fin=open("school.txt","r")
    s=fin.readlines()
    count_lines=0
    for j in s:
       count_lines=count_lines+1
    print("Total no of lines", count_lines)
    fin.close()

while True:
        print("\n Choose Options To : ")
        print("1. Count no of Characters")
        print("2. Count no of Words")
        print("3. Count no of lines")
        print("4. Exit")
        choice = int(input("Enter Your Choice :"))
        if choice==1 :
                    countchar()
        elif choice==2 :
                    countword()
        elif choice==3 :    
                    countline()
        elif choice==4:
                    break
        else :
                print("Invalid Choice")