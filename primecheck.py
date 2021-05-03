import random
import modular_functions

#generates random integers between 2 numbers
def random_between(n1,n2):
   return random.randrange(n1, n2,1)


def MillerTest(n,m):
    a = random_between(2,n-2)
    x = modular_functions.modpow(a,m,n)
    if(x == 1 or x == n-1):
        return True
    while(m != n-1):
        x = (x*x) % n;
        m= m*2
        if(x==1):
            return False
        if(x==n-1):
            return True
    return False


def isprime(n,k):
    i =0

    if(n<=1 or n == 4):
        return False
    if(n<=3):
        return True
    m = n-1
    while(m % 2 == 0):
        m = m//2
    for i in k:
        if(not MillerTest(n,int(m))):
            return False
    return True