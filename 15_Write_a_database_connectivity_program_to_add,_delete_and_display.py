#program to add delete and display student
import mysql.connector
con=mysql.connector.connect(host="localhost", user="root", passwd="password123") 
cur=con.cursor()
#Creating Database 
cur.execute("DROP DATABASE IF EXISTS Data")
cur.execute("create database Data")
cur.execute("use Data")
#Creating  Table 
cur.execute("drop table if exists Students")
cur.execute("create table students(Stname char(20),Class char(10),Section char(5))")
 
def ADDSTUDENT():
        global cn,cur
        print("******************* ADD NEW STUDENT *******************")
        Stname=input('enter student name')
        Class = input("Enter Class:")
        Section = input("Enter Section :")
        query="insert into Students values("+"'"+Stname+"'"+','+"'"+Class+"'"+','+"'"+Section+"'"+")"
        cur.execute(query)
        con.commit()
        print("/n record added successfully")
def DISPSTUDENT():
    global cn,cur
    try:
            query="select * from Students"
            cur.execute(query)
            results = cur.fetchall()
            print("**************************************************")
            print("STUDENT NAME"+"\t"+"CLASS"+"\t"+"SECTION")
            print("**************************************************")
            for row in results:
                print(row[0],"\t\t",row[1],"\t\t",row[2])
    except:
        print("error")
def DELETESTUDENT():
        global cn,cur
        print('********************** DELETE STUDENT****************************')
        en = input("Enter Student Name to delete :")
        query="select * from Students where Stname='"+en+"'"
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print("\## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
            print("**************************************************")
            print("STUDENT NAME"+"\t"+"CLASS"+"\t"+"SECTION")
            print("**************************************************")
            for row in results:
                print(row[0],"\t\t",row[1],"\t\t",row[2])
        ans = input("Are you sure to delete ? (y/n)")
        if ans=="y" or ans=="Y":
            query="delete from Students where Stname='"+en+"'"
            cur.execute(query)
            con.commit()
        print("/n record deleted")
            

def main():
    global cn,cur
    while True:
        print("1. ADD NEW STUDENT")
        print("2. DISPLAY STUDENTS")
        print("3. REMOVE A STUDENT")
        print("0. EXIT")
        ans = int(input("Enter your choice :"))
        if ans==1:
            ADDSTUDENT()
        elif ans==2:
            DISPSTUDENT()
        elif ans==3:
            DELETESTUDENT()
        elif ans==0:
            print("\nBye!!")
            cur.close()
main()
    
    
