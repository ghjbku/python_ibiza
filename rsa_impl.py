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


def enc(m,e,n):
    return modular_functions.modpow(m,e,n)


def dec(c,d,n):
    return modular_functions.modpow(c,d,n)


def RSA_run_enc(m,d,e,n,p,q):
    c = enc(m,e,n)
    return c


def RSA_run_dec(c,d,n,p,q):
    message = dec(c,d,n)
    mp =dec(c,d,p)
    mq =dec(c,d,q)
    return mp


#creates a list of characters from the string
def string_to_charlist(string):
    return list(string)


#creates a list of integers from the character list
def charlist_to_intlist(charlist):
    intlist = []
    for character in charlist:
        integer = ord(character)
        intlist.append(integer)
    return intlist


def RSA_for_message_enc(intlist,d,e,n,p,q):
    encrypted_int_list = []
    for integer in intlist:
        c = RSA_run_enc(integer,d,e,n,p,q)
        encrypted_int_list.append(c)
    return encrypted_int_list


def RSA_for_message_dec(encrypted_int_list,d,n,p,q):
    decrypted_int_list = []
    for integer in encrypted_int_list:
        mp = RSA_run_dec(integer,d,n,p,q)
        decrypted_int_list.append(mp)
    return decrypted_int_list


def decrypted_int_list_to_char_list(decrypted_int_list):
    dec_char_list = []
    for integer in decrypted_int_list:
        char = chr(integer)
        dec_char_list.append(char)
    return dec_char_list


def dec_char_list_to_string(dec_char_list):
    return "".join(dec_char_list)


#driver code here
def main(text):
    charlist = string_to_charlist(text)
    intlist = charlist_to_intlist(charlist)
    d,e,n,p,q = secret_key_gen()
    encrypted_int_list = RSA_for_message_enc(intlist,d,e,n,p,q)
    decrypted_int_list = RSA_for_message_dec(encrypted_int_list,d,n,p,q)
    print("encrypted values:")
    print(encrypted_int_list)
    dec_char_list = decrypted_int_list_to_char_list(decrypted_int_list)
    print(dec_char_list_to_string(dec_char_list))
    return

main("something fun pls")