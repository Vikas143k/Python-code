# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:11:58 2021

@author: writv
"""
# Program to add and display Book details
import mysql.connector 
#Connection to MySQL Server and database  
con = mysql.connector.connect(host="localhost", user="root", passwd="password123") 
cur = con.cursor() 
#Creating Database 
cur.execute("DROP DATABASE IF EXISTS Book") 
cur.execute("CREATE DATABASE Book") 
cur.execute("USE Book") 
#Creating  Table 
cur.execute("DROP TABLE IF EXISTS Books") 
cur.execute("CREATE TABLE Books(Bookname varchar(30), Rate int, Qty int, Author varchar(30) )") 

def ADDBOOK():
    global cn,cur
    print("*******************ADD NEW  **************************")
    Bookname = input("Enter Book Name :")
    Rate = int(input("Enter Rate:"))
    Qty = int(input("Enter Quantity :"))
    Author=input("Enter Author Name :")
    query="insert into Books values("+"'"+Bookname+"'"+','+str(Rate)+','+str(Qty)+','+"'"+Author+"'"+")"
    cur.execute(query)
    con.commit()
    print("\n ## RECORD ADDED SUCCESSFULLY!")

def DISPBOOK():
    global cn,cur
    try:
        query="select * from Books"
        cur.execute(query)
        results = cur.fetchall()
        print("**************************************************")
        print("BOOK NAME"+"\t\t"+"RATE"+"\t"+"QTY"+"\t"+"AUTHOR")
        print("**************************************************")
        for row in results:
            print(row[0],"\t\t",row[1],"\t\t",row[2],"\t\t",row[3])
    except:
       print("error")

while True:
    print("1. ADD BOOK")
    print("2. DISPLAY BOOKS")
    print("0. EXIT")
    ans = int(input("Enter your choice :"))
    if ans==1:
        ADDBOOK()
    elif ans==2:
        DISPBOOK()
    elif ans==0:
        print("\nBye!!")
        cn.close()

