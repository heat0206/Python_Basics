def convert(s):
    s1=''
    s.strip()
    lst1=s.split(' ')
    set1= set(lst1)
    lst2=list(set1)
    lst2.sort()
    for i in lst2:
        s1+=i
        

    return (' '.join(s1))

s=input('Enter string:')
print(convert(s))

