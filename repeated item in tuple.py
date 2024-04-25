#Write a Python program to find the repeated items of a tuple
tuple1=(0,1,2,3,4,4,5,6,6,7,7,8,8,8,4,6,3,5,3,6,4,5)
list1=[]
list1=list(tuple1)
print(list1)
for element in list1:
    a=list1.count(element)
    if a>=2:
        print(f"{element} is repeated {a} times")
    for second_element in list1:
        if second_element==element:
            list1.remove(second_element)