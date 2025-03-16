def ispangram(a):
    b=''
    for i in a:
        i=i.lower()
        if i!=' ':
            b+=i
        
    set1=set(b)
    set2={chr(i) for i in range(97,122)}

    if set2<=set1:
        print('is pangram')
    else:
        print('not pangram')

a=input('Enter sentence:')
ispangram(a)
