# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:17:08 2021

@author: writv
"""

# Program to Add,Search and Display Employee details 
import mysql.connector
cn = mysql.connector.connect(host='localhost',user='root',password="password123")
cur = cn.cursor()
cur.execute("DROP DATABASE IF EXISTS Comp") 
cur.execute("CREATE DATABASE Comp") 
cur.execute("USE Comp") 
cur.execute("DROP TABLE IF EXISTS compemp") 
cur.execute("CREATE TABLE compemp(empno int, ename VARCHAR(20), dept varchar(20), salary int)") 

def showAll():
    global cn,cur
    try:
        query="select * from compemp"
        cur.execute(query)
        results = cur.fetchall()
        print("**************************************************")
        print("EMPNO       EMP NAME      DEPARTMENT      SALARY")
        print("**************************************************")
        for row in results:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3])
    except:
        print("error")

def addEmp():
    global cn,cur
    print("*******************ADD NEW EMPLOYEE**************************")
    eno = int(input("Enter employee number :"))
    en = input("Enter employee name :")
    dp = input("Enter department ")
    sl = int(input("Enter Salary :"))
    query="insert into compemp values("+str(eno)+",'"+en+"','"+dp+"',"+str(sl)+")"
    cur.execute(query)
    cn.commit()
    print("\n ## RECORD ADDED SUCCESSFULLY!")
    
def searchEmp():
    global cn,cur
    print("*******************SEARCH EMPLOYEE **************************")
    en = int(input("Enter Employee number to search :"))
    query="select * from compemp where empno="+str(en)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print("EMPNO       EMP NAME      DEPARTMENT      SALARY")
        print("**************************************************")
        for row in results:
            print(row[0],"\t\t",row[1],"\t\t",row[2],"\t\t",row[3])
            
while True:
    print("1. SHOW EMPLOYEE LIST ")
    print("2. ADD NEW EMPLOYEE")
    print("3. SEARCH EMPLOYEE ")
    print("0. EXIT")
    ans = int(input("Enter your choice :"))
    if ans==1:
        showAll()
    elif ans==2:
        addEmp()
    elif ans==3:
        searchEmp()
    elif ans==0:
        print("\nBye!!")
        cn.close()
        break  
