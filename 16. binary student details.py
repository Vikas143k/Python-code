# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:34:40 2021

@author: writv
"""

# Program to Add Students Data and Display the data using binary file
import pickle
def Display():
        Myfile=open ('Student.dat','rb')
        print("\n-------DISPALY STUDENTS DETAILS--------")
        print("\nRoll No.",'\t ','Name','\t\t','Percetage','\t','Remarks')
        while True:
           try:
               rec=pickle.load(Myfile)
               print(' ',rec['SROLL'],'\t\t' ,rec['SNAME'],'\t\t',rec['SPERC'],'\t\t',rec['SREMARKS'])
           except EOFError:
                break
def Input():
    n=int(input("How many records you want to create :"))
    for ctr in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        sperc=float(input("Enter Percentage: "))
        sremark=input("Enter Remark: ")
        Myfile=open ('Student.dat','ab')
        srecord={"SROLL":sroll,"SNAME":sname,"SPERC":sperc,
                 "SREMARKS":sremark}        
        pickle.dump(srecord,Myfile)


while True:
        print('\nYour Choices are: ')
        print('1.Add Student')
        print('2.Dispaly Students') 
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            Input()
        elif ch==2:
            Display()
        else:
            break
