#Function to get prime factors using 'recursion'
def prime_factors(n,divisor=2,factors=None):
    if factors is None:
        factors=[]
    if n==1:
        return factors

    if n%divisor==0:
        factors.append(divisor)
        return prime_factors(n//divisor,divisor,factors)
    if divisor ==2:
        n_divisor=divisor+1
    else:
        n_divisor=divisor+2
    return prime_factors(n,n_divisor,factors)

n=int(input('Enter a number:'))
print(prime_factors(n))
