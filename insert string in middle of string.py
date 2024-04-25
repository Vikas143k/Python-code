# a Python function to insert a string in the middle of a string
str="my name is vikas yadav"
str2=input("Enter the word you want to insert>>")
length=len(str)
middle=round(length/2)
print(str[:middle] + str2 + str[middle:])
