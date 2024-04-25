# a Python program to count the occurrences of each word in a given sentence
a={}
str="vikas is a boy " \
    "vikas loves to be a boy " \
    "vikas tries to be a boy"
words=str.split()
for word in words:
    if word in a:
        a[word]+=1
    else:
        a[word]=1
print(a)