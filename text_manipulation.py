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