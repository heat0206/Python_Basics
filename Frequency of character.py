#Frequency of char
a=input('Enter a string:')
lst=list(a)
dict1={}
for i in lst:      
    dict1[i]=lst.count(i)

print(dict1)
