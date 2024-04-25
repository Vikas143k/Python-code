# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:20:02 2021

@author: writv
"""

# Program to add employee details to a csv file and read and display the contents
import csv
def addemp():
  with open('csvfile.csv','a', newline="") as csvf:
    writecsv=csv.writer(csvf,delimiter=',')
    choice='y'
    while choice.lower()=='y':
        eno=int(input("Enter Employee No."))
        en=input("Enter Employee Name")
        sal=float(input("Enter Salary"))
        dept=input("Enter Department")
        writecsv.writerow([eno,en,sal,dept])
        print(" Data saved in file..")
        choice=input("Want add more record(y/n).....")
  csvf.close()
  
def dispemp():
  with open('csvfile.csv','r')as csvf:
    readCSV =csv.reader(csvf,delimiter=',')
    for row in readCSV:
        print(row)
  csvf.close()
while True:
        print('\nYour Choices are: ')
        print('1.Add Employee Details')
        print('2.Dispaly Employee Details') 
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            addemp()
        elif ch==2:
            dispemp()
        else:
            break

