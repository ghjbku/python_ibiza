import random
import modular_functions
import primecheck


def random_number_gen(lengthofnumber):
    return random.getrandbits(lengthofnumber)


def RSA_prime_gen(lengthofnumber):
    n1= random_number_gen(lengthofnumber)
    index = 0;
    while(primecheck.isprime(n1,[40])==False):
        index=index+1;
        n1= random_number_gen(lengthofnumber)
    return n1;


# creating the data with the given length
def RSA_data_creation(lengthofnumber):
    p = RSA_prime_gen(lengthofnumber)
    print("p done")
    q = RSA_prime_gen(lengthofnumber)
    print("q done")
    n = p*q
    fi_n=(p-1)*(q-1)
    return n,fi_n,p,q

# creating an e, that has a gcd of 1 with fi_n 
def random_e(fi_n):
    e= primecheck.random_between(1,fi_n)
    gcd,x,y = modular_functions.ext_euc(e,fi_n)
    while(gcd != 1):
        e= primecheck.random_between(1,fi_n)
        gcd,x,y = modular_functions.ext_euc(e,fi_n)
    return e

# generating the secret key and return it with all the basic data
def secret_key_gen():
    n,fi_n,p,q = RSA_data_creation(128)
    e = random_e(fi_n)
    d = modular_functions.modinvers(e,fi_n)
    return d,e,n,p,q