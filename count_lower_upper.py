def count_lower_upper(a):
    u=0
    l=0
    for i in a:
        if 97<ord(i)<122:
            l+=1
        elif 65<ord(i)<90:
            u+=1
    dict1={}
    dict1={'Upper Case':u,'Lower Case':l}
    return dict1

a=input('Enter a string:')
print(count_lower_upper(a))
