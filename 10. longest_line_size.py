# program to display the longest line and size of the line  in a text file 
f=open("school.txt","w")
while True:
    line=input("Enter a line : ")
    f.write(line)
    f.write("\n")
    cont=input("do you want to continue?")
    if cont=="n":
        break
f.close()
    
fin=open("school.txt","r")
ctr=fin.read()
print(ctr)
fin.close()

f=open("school.txt","r")
large_line = ''
large_line_len = 0
for line in f:
       if len(line) > large_line_len:
              large_line_len = len(line)
              large_line = line
print("Largest line is :",large_line)                
print("Length of largest Line is :",large_line_len)          
f.close()
