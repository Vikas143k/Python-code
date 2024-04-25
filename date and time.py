#Write a Python program to display the current date and time
import datetime
b=datetime.datetime.now()
c=b.strftime("%x")
d=b.strftime("%X")
print(f"Today's date is {c}.")
print(f"The time is {d}.")