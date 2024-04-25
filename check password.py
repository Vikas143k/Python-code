#program to check for valid pass
passw="mysuru"
for p in range(1,4):
    p=input("enter password")
    if p==passw:
       print("login was successful")
    else:
        print("try again")
if p==passw:
   print("signing in.....")
else:
    print("try again later")
