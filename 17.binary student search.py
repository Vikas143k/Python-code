# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:37:18 2021

@author: writv
"""

# Program to add student details to a binary file and search a student nased on rollno
import pickle
def Readrecord():
        Myfile=open ('Student1.dat','rb')
        print("\n-------DISPALY STUDENTS DETAILS--------")
        print("\nRoll No.",'\t ','Name','\t\t','Percetage','\t','Remarks')
        while True:
           try:
               rec=pickle.load(Myfile)
               print(' ',rec['SROLL'],'\t\t' ,rec['SNAME'],'\t\t',rec['SPERC'],'\t\t',rec['SREMARKS'])
           except EOFError:
                break
def Input():
    Myfile=open ('Student1.dat','ab')
    n=int(input("How many records you want to create :"))
    for ctr in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        sperc=float(input("Enter Percentage: "))
        sremark=input("Enter Remark: ")
        srecord={"SROLL":sroll,"SNAME":sname,"SPERC":sperc,
                 "SREMARKS":sremark}        
        pickle.dump(srecord,Myfile)
def Search(roll):
        Myfile=open ('Student1.dat','rb')
        print("\nRoll No.",'\t ','Name','\t\t','Percetage','\t','Remarks')
        while True:
         try:
               rec=pickle.load(Myfile)
               if rec['SROLL']==roll:
                 print(' ',rec['SROLL'],'\t\t' ,rec['SNAME'],'\t\t',rec['SPERC'],'\t\t',rec['SREMARKS'])
                 found =1
         except EOFError:
                break
        else:
                found=0
        if found==0:
            print("Record not found")
while True:
        print('\nYour Choices are: ')
        print('1.Add Student Details')
        print('2.Dispaly Deatils') 
        print('3.Search Student')
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            Input()
        elif ch==2:
            Readrecord()
        elif ch==3:
            r =int(input("Enter a Rollno to search: "))
            Search(r)
        else:
            break
