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
    d,e,n,p,q = RSA_data.secret_key_gen()
    encrypted_int_list = RSA_for_message_enc(intlist,d,e,n,p,q)
    decrypted_int_list = RSA_for_message_dec(encrypted_int_list,d,n,p,q)
    print("encrypted values:")
    print(encrypted_int_list)
    dec_char_list = decrypted_int_list_to_char_list(decrypted_int_list)
    print(dec_char_list_to_string(dec_char_list))
    return

main("something fun pls")