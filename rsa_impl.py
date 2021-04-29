import modular_functions
import RSA_data
import rsa_methods

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
    encrypted_int_list = rsa_methods.RSA_for_message_enc(intlist,d,e,n,p,q)
    decrypted_int_list = rsa_methods.RSA_for_message_dec(encrypted_int_list,d,n,p,q)
    print("encrypted values:")
    print(encrypted_int_list)
    dec_char_list = decrypted_int_list_to_char_list(decrypted_int_list)
    print(dec_char_list_to_string(dec_char_list))
    return

main("something fun pls")