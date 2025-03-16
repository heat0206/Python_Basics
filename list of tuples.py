def square_cube(n):
    lst=[]
    for i in range (1,n+1):
        tp=(i,i**2,i**3)
        lst.append(tp)

    return lst

n=int(input('Enter ending value:'))
print(square_cube(n))
