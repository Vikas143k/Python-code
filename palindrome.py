#a program check whether a number is palindrome or not
num=int(input("enter a number"))
n=num
reverse=0
while(num>0):
    remain=num%10
    reverse=reverse*10+remain
    num=num//10
if reverse==n:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
