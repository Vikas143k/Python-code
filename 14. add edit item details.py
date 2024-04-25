# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 01:18:26 2021

@author: writv
"""

# Program to add, edit and display Item details
import mysql.connector 
#Connection to MySQL Server and database student 
con = mysql.connector.connect(host="localhost", user="root", passwd="password123") 
cur = con.cursor() 
#Creating Database 
cur.execute("DROP DATABASE IF EXISTS Shop") 
cur.execute("CREATE DATABASE Shop") 
cur.execute("USE Shop") 
#Creating  Table 
cur.execute("DROP TABLE IF EXISTS Item") 
cur.execute("CREATE TABLE Item(Itname varchar(30), Rate int, Qty int)") 
def ADDITEM():
    global cn,cur
    print("*******************ADD NEW ITEM **************************")
    Itname = input("Enter Item Name :")
    Rate = int(input("Enter Rate:"))
    Qty = int(input("Enter Quantity :"))
    query="insert into Item values("+"'"+Itname+"'"+','+str(Rate)+','+str(Qty)+")"
    cur.execute(query)
    con.commit()
    print("\n ## RECORD ADDED SUCCESSFULLY!")

def DISPITEM():
    global cn,cur
    try:
        query="select * from Item"
        cur.execute(query)
        results = cur.fetchall()
        print("**************************************************")
        print("ITEM NAME"+"\t"+"RATE"+"\t"+"QTY")
        print("**************************************************")
        for row in results:
            print(row[0],"\t\t",row[1],"\t\t",row[2])
    except:
       print("error")
def EDITITEM():
    global cn,cur
    print("*******************EDIT ITEM **************************")
    en = input("Enter Item name to edit :")
    query="select * from Item where Itname='"+en+"'"
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
    else:
       
        print("**************************************************")
        print("ITEM NAME"+"\t"+"RATE"+"\t"+"QTY")
        print("**************************************************")
        for row in results:
            print(row[0],"\t\t",row[1],"\t\t",row[2])
    print("-"*50)
    ans = input("Are you sure to update ? (y/n)")
    if ans=="y" or ans=="Y":
        d = int(input("Enter new rate to update (enter old value if not to update) :"))
        s = int(input("Enter new quantity to update (enter old value if not to update) :"))
        query="update Item set rate='"+str(d)+"',Qty='"+str(s) + "' where Itname='"+str(en)+"'"
        cur.execute(query)
        con.commit()
        print("\n## RECORD UPDATED  ##")

def main():
 global cn,cur  
 while True:
    print("1. ADD NEW ITEM")
    print("2. DISPLAY ITEMS")
    print("3. EDIT ITEM ")
    print("0. EXIT")
    ans = int(input("Enter your choice :"))
    if ans==1:
        ADDITEM()
    elif ans==2:
        DISPITEM()
    elif ans==3:
        EDITITEM()
    elif ans==0:
        print("\nBye!!")
        cn.close()
main()
