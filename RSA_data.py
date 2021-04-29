import random
import modular_functions
import primecheck


def random_number_gen(lower,upper):
    return primecheck.random_between(random.getrandbits(lower),int((random.getrandbits(lower)+random.getrandbits(upper))*1.5))


def RSA_prime_gen(lower,upper):
    n1= random_number_gen(lower,upper)
    index = 0;
    while(not primecheck.isprime(n1,[1,2])):
        index=index+1;
        n1= random_number_gen(lower,upper)
    #print("primegen:"+str(n1)+" index: "+str(index))
    return n1;


def RSA_n_fin(min,max):
    p = RSA_prime_gen(min,max)
    q = RSA_prime_gen(min,max)
    n = p*q
    fi_n=(p-1)*(q-1)
    return n,fi_n,p,q


def random_e(fi_n):
    e= primecheck.random_between(1,fi_n)
    gcd,x,y = modular_functions.ext_euc(e,fi_n)
    while(gcd != 1):
        e= primecheck.random_between(1,fi_n)
        gcd,x,y = modular_functions.ext_euc(e,fi_n)
    return e


def secret_key_gen():
    n,fi_n,p,q = RSA_n_fin(30,35)
    e = random_e(fi_n)
    #print("n:"+str(n)+"\nfi_n:"+str(fi_n)+"\ne:"+str(e))
    d = modular_functions.modinvers(e,fi_n)
    return d,e,n,p,q