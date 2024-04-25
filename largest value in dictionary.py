#Python program to find the highest 3 values of corresponding keys in a dictionary
dic1={'A': 5, 'B': 56, 'hobby': 26,"d":234}
list1=[]
a=0
for i in dic1.keys():
    list1.append(dic1.get(i))
list1.sort(reverse=True)
print("Dictionary with 3 highest values:")
print("Keys:Values")
for i in list1:
    for key, value in dic1.items():
        if value==i and a<3:
            print(key," : ",i)
            a+=1


