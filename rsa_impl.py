import modular_functions
import RSA_data
import rsa_methods
import text_manipulation


def main(text):
    charlist = text_manipulation.string_to_charlist(text)
    intlist = text_manipulation.charlist_to_intlist(charlist)
    d,e,n,p,q = RSA_data.secret_key_gen()
    encrypted_int_list = rsa_methods.RSA_for_message_enc(intlist,d,e,n,p,q)
    decrypted_int_list = rsa_methods.RSA_for_message_dec(encrypted_int_list,d,n,p,q)
    print("encrypted values:")
    print(encrypted_int_list)
    dec_char_list = text_manipulation.decrypted_int_list_to_char_list(decrypted_int_list)
    print(text_manipulation.dec_char_list_to_string(dec_char_list))
    return

main("something fun pls")