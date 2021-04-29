import modular_functions
import RSA_data

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