def create_array(a,b,c,d):
    arr=[[[d for i in range(a)]for i in range(b)]for i in range(c)]

    return arr


a= int(input('Enter a:'))
b= int(input('Enter b:'))
c= int(input('Enter c:'))
d= int(input('Enter d:'))


print(create_array(a,b,c,d))

