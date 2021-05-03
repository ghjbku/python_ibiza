import modular_functions
import RSA_data
import rsa_methods
import text_manipulation
import time
start_time = time.time()

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

#message_to_encrypt ="Zu An blinked in surprise. “You want me to rile Yuan Wendong up once more?” He’d never expected such a suggestion out of his wife.\nChu Chuyan thought that Zu An might be feeling intimidated, so she added, “Don’t worry, I’ll accompany you tomorrow. No matter how you rile him up, I’ll be there to ensure your safety.”\nWoah, what’s with this sudden declaration that almost sounds like a confession? Why does it feel like our positions have been reversed… Well, I guess it’s fine. Mooching off others is pretty cool after all.\nZu An nodded affirmatively. “Rest assured, honey. Since you’ve decreed it, I’ll make sure to blow him up with rage!”\nThe way Zu An referred to Chu Chuyan as ‘honey’ brought frowns to Chu Chuyan and Qin Wanru’s faces, but neither made any further comment.\n“Big sister, you’ll be heading to the academy tomorrow?” asked Chu Huanzhao.\n“I am. What’s with your expression?” asked Chu Chuyan with a smile. “Could it be that you’ve stirred trouble in the academy, and you’re worried that the teachers will complain to me?”\n“Of course not! It’s just that you haven’t been to the academy for quite some time now. I’m just delighted,” Chu Huanzhao replied indignantly, directing a secret wink at Zu An. “Speaking of which, doesn’t the Sky class have an arithmetic class tomorrow?”\n“That’s right,” replied Chu Chuyan. “Actually, most of the cultivation classes in the academy don’t serve much purpose to me anymore. These arithmetic classes are far more useful. After all, the Chu clan has many finance-related matters that need dealing with.”\nChu Huanzhao tried her best to suppress her smile, her face straining with the effort. “It just so happens that the academy brought in a new arithmetic teacher. He might be more to your liking.”\n“They’ve changed the arithmetic teacher? What happened to Yang Wei?” Chu Chuyan was surprised to hear that news. She had been so busy dealing with the affairs in the Chu clan that she hadn’t paid any attention to the recent happenings in the academy.\n“It seems like Yang Wei has been fired for oppressing his students,” replied Chu Huanzhao vaguely.\nChu Chuyan took her time to reply. “I can’t deny that Yang Wei has some serious character flaws. However, his skills in arithmetic are the real deal. I’m not sure if the new teacher will be able to fill his shoes.”"
message_to_encrypt="molylepkefasz"
main(message_to_encrypt)
print("\n--- %s seconds ---" % (time.time() - start_time))